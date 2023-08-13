from policyengine_canada.model_api import *


class qc_solidarity_northern_village_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec solidarity tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.solidarity.amount.northern_village

        # family situation
        married = household("is_married", period)
        children = household("count_children", period)

        northern_village_eligible = household(
            "qc_living_in_northern_villages", period
        )

        northern_village_children_amount = children * p.child
        northern_village_spouse_amount = married * p.spouse

        return northern_village_eligible * (
            p.base
            + northern_village_spouse_amount
            + northern_village_children_amount
        )
