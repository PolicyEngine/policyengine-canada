from policyengine_canada.model_api import *


class climate_action_incentive_single_parent_household(Variable):
    value_type = bool
    entity = Household
    label = "Canada Climate Action single parent status"
    unit = CAD
    documentation = "Determination wether the filer is a single parent eligible for the climate action incentive"
    definition_period = YEAR

    def formula(household, period, parameters):
        married = household("is_married", period)
        cai_children = household(
            "climate_action_incentive_dependent_children", period
        )
        return ~married & (cai_children > 0)
