from policyengine_canada.model_api import *


class is_infirm_relative(Variable):
    value_type = bool
    entity = Person
    label = "Is an adult infirm relative of the household"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("age", period) >= 18
