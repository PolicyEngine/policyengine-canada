from policyengine_canada.model_api import *


class child_benefit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Canada Child Benefit"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("child_benefit_base_person", period) > 0
