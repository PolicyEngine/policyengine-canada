from policyengine_canada.model_api import *


class is_first_child(Variable):
    value_type = bool
    entity = Household
    label = "Is the first born child in a Household"
    definition_period = YEAR
