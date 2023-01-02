from policyengine_canada.model_api import *


class household_members(Variable):
    value_type = float
    entity = Household
    label = "Members in household"
    definition_period = YEAR
    default_value = 1.0
