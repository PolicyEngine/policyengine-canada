from policyengine_canada.model_api import *


class is_widow(Variable):
    value_type = bool
    entity = Person
    label = "Widow or widower"
    documentation = "Spouse or common-law partner has died and since their death the person has not remarried or become a common-law partner to another person"
    definition_period = YEAR
