from policyengine_canada.model_api import *


class is_disabled_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Is a disabled dependant"
    definition_period = YEAR

    # Impute dependant status on disability.
    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        dependant = person("is_adult_dependant", period)
        return disabled * dependant