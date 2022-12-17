from policyengine_canada.model_api import *


class canada_workers_benefit_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Canada workers benefit dependant"
    definition_period = YEAR
    reference = ""  # TODO: Add

    def formula(person, period, parameters):
        return ~person("canada_workers_benefit_eligible", period)
