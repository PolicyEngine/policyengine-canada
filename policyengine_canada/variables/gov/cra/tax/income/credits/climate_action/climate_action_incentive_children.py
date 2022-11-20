from policyengine_canada.model_api import *


class climate_action_incentive_children(Variable):
    value_type = float
    entity = Household
    label = "Combined Canada Climate Action for all children"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        children = household("children", period)
        province = household("province_str", period)
        children_amount = parameters(
            period
        ).gov.cra.tax.income.credits.climate_action_incentive.amount.child[
            province
        ]
        return children * children_amount
