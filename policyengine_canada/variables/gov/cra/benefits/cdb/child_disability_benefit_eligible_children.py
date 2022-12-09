from policyengine_canada.model_api import *


class child_disability_benefit_eligible_children(Variable):
    value_type = float
    entity = Person
    label = "Children eligible for Canada Child Disability Benefit"
    unit = "Person"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        disabled = person("is_dsiabled")
        return disabled & (age < 18)
