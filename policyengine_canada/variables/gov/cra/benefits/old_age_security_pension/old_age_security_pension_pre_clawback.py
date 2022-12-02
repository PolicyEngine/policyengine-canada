from policyengine_canada.model_api import *

# SPSD/M 29.0: imioas or imoasmax, I'm not sure. I think imioas is post-clawback?

class old_age_security_pension_pre_clawback(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension pre-clawback"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        adult_years_in_canada = person("adult_years_in_canada", period)
        eligible = person("old_age_security_pension_eligibility", period)
        oas_pension = parameters(
            period
        ).gov.cra.benefits.old_age_security_pension  # shortcut
        older_increase_age_threshold = (
            oas_pension.age_eligibility_older_seniors_increase
        )  # age at which you get the percentage boost
        eligible_older_increase = age >= older_increase_age_threshold
        total_older_increase_factor = (
            1
            + eligible_older_increase
            * oas_pension.amount.older_seniors_increase_factor
        )
        base_amount = oas_pension.amount.base
        scale_factor = min(
            adult_years_in_canada / oas_pension.residence_for_full_base_amount,
            1,
        )  # Your full base amount is your number of adult residence years divided by the number of years at which you are eligible for 100%. In the SPSD/M 29.0 this is imoasres
        return (
            eligible
            * base_amount
            * scale_factor
            * total_older_increase_factor
        )  # apply the old age boost to the base amount if applicable. In the SPSD/M 29.0 this is imoasmax
