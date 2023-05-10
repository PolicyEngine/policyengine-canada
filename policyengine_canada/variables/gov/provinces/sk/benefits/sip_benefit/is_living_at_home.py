from policyengine_canada.model_api import *


class is_living_at_home(Variable):
    value_type = bool
    entity = Household
    label = "Client Category is living at home"
    definition_period = YEAR