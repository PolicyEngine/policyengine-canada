from policyengine_canada.model_api import *


class old_age_security_pension_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Old age security pension eligibility"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        age = tax_unit("age", period)
        adult_years_in_canada = tax_unit("adult_years_in_canada", period)
        oas_pension = parameters(
            period
        ).gov.cra.benefits.old_age_security_pension
        eligible_age_threshold = oas_pension.age_eligibility
        eligible_residence_threshold = (
            oas_pension.residence_eligibility
        )  # Specifically years resident over the age of 18
        eligible = (age >= eligible_age_threshold) & (
            adult_years_in_canada >= eligible_residence_threshold
        )
        return eligible
