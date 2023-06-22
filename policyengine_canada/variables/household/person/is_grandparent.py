from policyengine_canada.model_api import *


class is_grandparent(Variable):
    value_type = bool
    entity = Person
    label = "Is one of spouse or head's' grandparents in a household"
    definition_period = YEAR
