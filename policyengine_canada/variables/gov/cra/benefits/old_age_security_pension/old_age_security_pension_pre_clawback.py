from policyengine_canada.model_api import *


class old_age_security_pension_pre_clawback(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension pre-clawback"
    unit = CAD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        age = tax_unit("age", period)
        adult_years_in_canada = tax_unit("adult_years_in_canada", period)
        oas_pension = parameters(period).gov.cra.benefits.old_age_security_pension
        # TODO: Add 10-year minimum.
        # TODO: Separate eligibility into a variable.
        eligible_age_threshold = oas_pension.age_eligibility
        eligible = age >= eligible_age_threshold
        older_increase_age_threshold = oas_pension.age_eligibility_older_seniors_increase
        eligible_older_increase = age >= older_increase_age_threshold
        total_older_increase_factor = 1 + eligible_older_increase * oas_pension.older_seniors_increase_factor
        maximum_amount = oas_pension.maximum_amount
        # TODO: turn the 40 into a parameter
        scale_factor = min_(adult_years_in_canada / 40, 1)
        return eligible * maximum_amount * scale_factor * total_older_increase_factors