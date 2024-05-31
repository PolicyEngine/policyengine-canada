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
        age = person("age", period)
        disabled = person("is_disabled", period)
        is_dependant = (age >= p.age_eligibility.upper) | (
            age >= p.age_eligibility.lower & disabled
        )

        income = person("individual_net_income", period)
        dependant_net_income = income * is_dependant

        income_eligibility = (
            dependant_net_income <= p.upper_dependant_income_threshold
        )

        net_income = max_(
            0, p.upper_dependant_income_threshold - dependant_net_income
        )

        cohabitating_dependant = person("cohabitating_dependant", period)

        caregiver_amount = (
            net_income * income_eligibility * cohabitating_dependant
        )

        return min_(caregiver_amount, p.max_amount)
