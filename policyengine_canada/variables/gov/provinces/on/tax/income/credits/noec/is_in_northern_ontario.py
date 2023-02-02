from policyengine_canada.model_api import *


class is_in_northern_ontario(Variable):
    value_type = bool
    entity = Household
    label = "Is located in Northern Ontario"
    definition_period = YEAR


# placeholder until district enum is made
