from policyengine_canada.model_api import *


class ab_caregiver_amount(Variable):
    value_type = float
    entity = Person
    label = "Alberta caregiver amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1ab/td1ab-23e.pdf"
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.credits_return

        # Whether the person is dependant (65 or older/ disabled)
        is_dependant = person("is_parent_or_grandparent", period) | (
            person("age", period)
            >= p.lower_age_eligibility & person("is_disabled", period)
        )
        dependant_net_income = (
            person("individual_net_income", period) * is_dependant
        )

        income_eligibility = (
            dependant_net_income <= p.upper_dependant_income_threshold
        )

        caregiver_amount = (
            p.upper_dependant_income_threshold - dependant_net_income
        ) * income_eligibility

        return min_(caregiver_amount, p.maximum_caregiver_amount)
