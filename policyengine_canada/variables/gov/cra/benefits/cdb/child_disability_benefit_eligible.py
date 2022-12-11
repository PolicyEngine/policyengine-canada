from policyengine_canada.model_api import *


class child_disability_benefit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Children eligible for Canada Child Disability Benefit"
    unit = "Person"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        disabled = person("is_disabled", period)
        return disabled & (age < 18)
