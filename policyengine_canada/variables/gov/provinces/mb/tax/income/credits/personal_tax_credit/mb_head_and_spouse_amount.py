from policyengine_canada.model_api import *


class mb_head_and_spouse_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba personal tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.personal_tax_credit

        head = person("is_head", period)

        age_eligibility = person("age", period) >= p.elderly_age_amount

        age_eligible_head = head & age_eligibility
        age_eligible_head_amount = age_eligible_head * p.age_credit
        disabled = person("is_disabled", period)

        # calculation of head and spouse credit amount
        head_spouse_amount = (
            head * p.basic_credit
            + age_eligible_head_amount
            + person("mb_spouse_credit_amount", period)
            + disabled * p.disability_credit
        )

        return head_spouse_amount
