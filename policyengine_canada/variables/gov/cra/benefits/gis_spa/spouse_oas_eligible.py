from policyengine_canada.model_api import *

class spouse_oas_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Spouse is eligible for the Old Age Security Pension"
    definition_period = YEAR

    def formula(person, period, parameters):
        oas_eligible = person("old_age_security_pension_eligibility", period)
        head_or_spouse = person("is_head", period) | person("is_spouse", period)
        head_or_spouse_oas_eligible = head_or_spouse & oas_eligible
        household = person.household
        count_head_or_spouse_oas_eligible = household.sum(head_or_spouse_oas_eligible)
        spouse_oas_eligible = count_head_or_spouse_oas_eligible - where(oas_eligible, 1, 0)

        return spouse_oas_eligible