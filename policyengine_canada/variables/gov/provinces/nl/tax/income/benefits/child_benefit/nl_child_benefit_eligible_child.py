from policyengine_canada.model_api import *

class nl_child_benefit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Newfoundland and Labrador child benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(period).gov.provinces.nl.benefits.child_benefits.child_eligible
        )
