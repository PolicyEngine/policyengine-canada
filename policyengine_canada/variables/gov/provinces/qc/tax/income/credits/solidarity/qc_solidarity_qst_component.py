from policyengine_canada.model_api import *


class qc_solidarity_qst_component(Variable):
    value_type = float
    entity = Household
    label = "Quebec Solidarity Tax Credit - QST Component"
    unit = CAD
    documentation = (
        "Quebec Sales Tax (QST) offset component of the Solidarity Tax Credit"
    )
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.solidarity.qst

        # Base amounts per person
        household_size = household("household_size", period)
        base_amount = household_size * p.per_person_amount

        # Income-tested reduction
        income = household("adjusted_family_net_income", period)
        reduction = p.reduction_rate * max_(0, income - p.threshold)

        return max_(0, base_amount - reduction)
