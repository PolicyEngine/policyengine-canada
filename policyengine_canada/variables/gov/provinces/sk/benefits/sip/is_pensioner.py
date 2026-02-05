from policyengine_canada.model_api import *


class is_pensioner(Variable):
    value_type = bool
    entity = Person
    label = "Is a pensioner"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("age", period) > 65