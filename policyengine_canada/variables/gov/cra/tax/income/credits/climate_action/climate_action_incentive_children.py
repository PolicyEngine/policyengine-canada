from policyengine_canada.model_api import *


class climate_action_children(Variable):
    value_type = float
    entity = Household
    label = "Canada Climate Action amount per child under 19"
    unit = CAD
    documentation = "Determination of the amount per child"
    definition_period = YEAR

    def formula(household, period, parameters):
        children = household("children", period)
        province = household("province_str", period)
        children_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action.amount.child[province]
        return children * children_amount
