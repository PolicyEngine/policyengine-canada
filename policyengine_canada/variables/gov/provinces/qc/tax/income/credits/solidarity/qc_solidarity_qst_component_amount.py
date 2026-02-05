from policyengine_canada.model_api import *


class qc_solidarity_qst_component_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec solidarity tax credit qst component"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.solidarity.amount.qst

        # child if married
        married = household("is_married", period)

        # QST component
        # Requires having paid some Quebec sales tax
        qst_eligible = add(household, period, ["qc_sales_tax"]) > 0

        qst_spouse_amount = married * p.spouse
        qst_living_alone_amount = ~married * p.living_alone

        return qst_eligible * (
            p.base + qst_spouse_amount + qst_living_alone_amount
        )
