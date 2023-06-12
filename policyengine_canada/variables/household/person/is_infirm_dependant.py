from policyengine_canada.model_api import *


class is_infirm_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Is a infirm dependant"
    definition_period = YEAR

    # Impute dependant status on age.
    def formula(person, period, parameters):
        return person("age", period) >= 18
