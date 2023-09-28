from policyengine_canada.model_api import *


class is_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Is a dependant in the household"
    definition_period = YEAR

    def formula(person, period, parameters):
        head = person("head", period)
        spouse = person("spouse", period)
        return ~head & ~spouse
