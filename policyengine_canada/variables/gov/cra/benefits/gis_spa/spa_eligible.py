from policyengine_canada.model_api import *

class spa_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Spouse is eligible for the Old Age Security Pension"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.gis_spa
        age = person("age", period)
        adult_years_in_canada = person("adult_years_in_canada", period)
        widow = person("is_widow", period)
        oas_eligible = person("old_age_security_pension_eligibility", period)
        spouse_oas_eligible = person("spouse_oas_eligible", period)
        return ~oas_eligible & (widow | spouse_oas_eligible) & (age >= p.spa_widows_eligibility_age) & (adult_years_in_canada >= p.spa_residency_requirement)