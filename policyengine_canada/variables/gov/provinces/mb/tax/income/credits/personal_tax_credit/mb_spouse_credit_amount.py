from policyengine_canada.model_api import *


class mb_spouse_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba spouse tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.personal_tax_credit

        spouse = person("is_spouse", period)
        age_eligibility = person("age", period) >= p.elderly_age_amount
        disabled = person("is_disabled", period)

        age_eligible_spouse = spouse & age_eligibility
        disabled_spouse = spouse & disabled

        spouse_credit_amount = (
            spouse * p.basic_credit
            + age_eligible_spouse * p.age_credit
            + disabled_spouse * p.disability_credit
        )

        return spouse_credit_amount
