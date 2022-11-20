from policyengine_canada.model_api import *


class climate_action_incentive_dependent_children(Variable):
    value_type = int
    entity = Household
    label = "Climate action incentive dependent Children"
    unit = CAD
    documentation = "Number of dependent children under the age of 19"
    definition_period = YEAR
