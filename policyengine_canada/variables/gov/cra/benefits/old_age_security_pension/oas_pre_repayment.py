from policyengine_canada.model_api import *

# SPSD/M 29.0: imioas or imoasmax, I'm not sure. I think imioas is post-repayment?


class oas_pre_repayment(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension pre-repayment"
    documentation = "The OAS amount a person is eligible for prior to the repayment tax. See SPSD/M 'imoasmax'."
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        adult_years_in_canada = person("adult_years_in_canada", period)
        oas_eligible = person("oas_eligibility", period)
        p = parameters(period).gov.cra.benefits.old_age_security_pension
        # Age at which you get the percentage boost.
        older_increase_age_threshold = p.eligibility.age.older_seniors_increase
        eligible_older_increase = age >= older_increase_age_threshold
        total_older_increase_factor = (
            1
            + eligible_older_increase * p.amount.older_seniors_increase_factor
        )
        base_amount = p.amount.base
        # Your full base amount is your number of adult residence years divided
        # by the number of years at which you are eligible for 100%.
        # In the SPSD/M 29.0 this is imoasres.
        residency_scale_factor = min_(
            adult_years_in_canada / p.eligibility.residence.full_base_amount,
            1,
        )
        # Apply the old age boost to the base amount if applicable.
        # In the SPSD/M 29.0 this is imoasmax.
        amount = (
            oas_eligible
            * base_amount
            * residency_scale_factor
            * total_older_increase_factor
        )

        return numpy.around(amount, 2)
