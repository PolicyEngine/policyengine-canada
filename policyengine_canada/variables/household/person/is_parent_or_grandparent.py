from policyengine_canada.model_api import *


class is_parent_or_grandparent(Variable):
    value_type = bool
    entity = Person
    label = "Is parent or grandparent"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("age", period) >= 65
