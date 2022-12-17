from policyengine_canada.model_api import *


class canada_workers_benefit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for canada workers benefit"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.cwb
        return person("age", period) >= p.eligible_age
