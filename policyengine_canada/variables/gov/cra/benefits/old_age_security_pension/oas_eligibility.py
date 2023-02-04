from policyengine_canada.model_api import *


class oas_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Old age security pension eligibility"
    unit = CAD
    documentation = "Eligibility for the OAS based on age and adult years resident in canada"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.cra.benefits.old_age_security_pension.eligibility
        age_eligible = person("age", period) >= p.age.base
        residency_eligible = (
            person("adult_years_in_canada", period) >= p.residence.any
        )
        return age_eligible & residency_eligible
