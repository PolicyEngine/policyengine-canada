from policyengine_canada.model_api import *


class climate_action_incentive_dependant_children(Variable):
    value_type = int
    entity = Household
    label = "Climate action incentive dependant Children"
    unit = CAD
    documentation = "Number of eligible dependant children"
    definition_period = YEAR

    adds = ["is_child_for_climate_action_incentive"]
