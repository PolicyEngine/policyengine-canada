from policyengine_canada.model_api import *


class is_grandparent(Variable):
    value_type = bool
    entity = Person
    label = "Is grandparent"
    definition_period = YEAR
