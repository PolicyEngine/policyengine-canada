from policyengine_canada.model_api import *


class is_in_northern_ontario(Variable):
    value_type = bool
    entity = Household
    label = "Is located in northern ontario"
    definition_period = YEAR


# placeholder until distric enum is made