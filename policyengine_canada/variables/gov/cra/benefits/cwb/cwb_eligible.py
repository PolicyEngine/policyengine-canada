from policyengine_canada.model_api import *


class cwb_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Canada Workers Benefit"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.cwb
        eligible_age = person("age", period) >= p.eligible_age
        family = person.household("is_cwb_family", period)
        any_of_eligible_age = person.household.any(eligible_age)
        return family | any_of_eligible_age
