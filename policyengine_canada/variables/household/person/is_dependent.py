from policyengine_canada.model_api import *


class is_dependent(Variable):
    value_type = bool
    entity = Person
    label = "Is a dependent"
    definition_period = YEAR

    # Impute dependent status on age.
    def formula(person, period, parameters):
        return person("age", period) < 18
