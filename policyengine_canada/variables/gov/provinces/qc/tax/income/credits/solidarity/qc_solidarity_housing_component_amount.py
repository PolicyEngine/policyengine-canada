from policyengine_canada.model_api import *


class qc_solidarity_housing_component_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec solidarity tax credit housing component"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.solidarity.amount.housing

        # family situation
        married = household("is_married", period)
        children = household("count_children", period)

        # Housing component
        housing_eligible = add(household, period, ["property_tax", "rent"]) > 0

        housing_family_amount = married * p.family
        housing_living_alone_amount = ~married * p.living_alone
        housing_children_amount = children * p.child

        return housing_eligible * (
            housing_family_amount
            + housing_living_alone_amount
            + housing_children_amount
        )
