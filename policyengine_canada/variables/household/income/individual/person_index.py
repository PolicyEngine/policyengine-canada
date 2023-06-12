from policyengine_canada.model_api import *


class person_index(Variable):
    value_type = int
    entity = Person
    label = "Person reference number, based on age"
    definition_period = YEAR

    def formula(person, period, parameters):
        # The person index, by age, descending.
        return person.get_rank(person.household, -person("age", period))
