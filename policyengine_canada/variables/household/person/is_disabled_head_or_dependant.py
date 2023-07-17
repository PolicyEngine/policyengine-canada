from policyengine_canada.model_api import *


class is_disabled_head_or_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Is a disabled dependant or head"
    definition_period = YEAR

    # Impute dependant and head status on disability.
    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        dependant = person("is_adult_dependant", period)
        head = person("is_head", period)
        return disabled * (dependant | head)