from policyengine_canada.model_api import *


class spa_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Person is eligible for the Spousal Allowance"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.gis_spa
        age = person("age", period)
        adult_years_in_canada = person("adult_years_in_canada", period)
        widow = person("is_widow", period)
        oas_eligible = person("oas_eligible", period)
        spouse_oas_eligible = person("spouse_oas_eligible", period)
        meets_residency_requirement = (
            adult_years_in_canada >= p.spa_residency_requirement
        )
        return (
            ~oas_eligible
            & meets_residency_requirement
            & (
                (widow & (age >= p.spa_widows_eligibility_age))
                | (spouse_oas_eligible & (age >= p.spa_spouse_eligibility_age))
            )
        )
