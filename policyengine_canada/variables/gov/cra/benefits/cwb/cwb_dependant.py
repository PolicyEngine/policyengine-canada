from policyengine_canada.model_api import *


class cwb_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Canada workers benefit dependant"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.cwb
        return person("age", period) < p.eligible_age
