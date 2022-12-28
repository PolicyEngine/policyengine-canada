from policyengine_canada.model_api import *


class cwb_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Eligible for Canada Workers Benefit"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        p = parameters(period).gov.cra.benefits.cwb
        eligible_age = person("age", period) >= p.eligible_age
        family = household("is_cwb_family", period)
        any_of_eligible_age = household.any(eligible_age)
        return family | any_of_eligible_age
