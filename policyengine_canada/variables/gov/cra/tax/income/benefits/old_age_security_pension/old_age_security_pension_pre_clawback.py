from policyengine_canada.model_api import *


class old_age_security_pension_pre_clawback(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension pre-clawback"
    unit = CAD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        age = tax_unit("age", period)
        income = tax_unit("old_age_security_pension_income", period)
        adult_years_in_canada = tax_unit("adult_years_in_canada", period)
        oas_pension = parameters(period).gov.cra.tax.income.benefits.old_age_security_pension
        eligible_age_threshold = oas_pension.age_eligibility
        eligible = age >= eligible_age_threshold
        older_increase_age_threshold = oas_pension.age_eligibility_older_seniors_increase
        eligible_older_increase = age >= older_increase_age_threshold
        older_increase_factor = oas_pension.older_seniors_increase_factor
        total_older_increase = (1 + older_increase_factor) if eligible_older_increase else 1
        maximum_amount = oas_pension.maximum_amount
        scale_factor = adult_years_in_canada / 40
        return eligible * maximum_amount * scale_factor * total_older_increase