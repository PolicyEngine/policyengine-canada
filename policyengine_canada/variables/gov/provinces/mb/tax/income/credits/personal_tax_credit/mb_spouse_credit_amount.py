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
        age_eligibility = person("born_year", period) <= p.age.elderly_age
        disabled = person("is_disabled", period)

        age_eligible_spouse = spouse & age_eligibility
        disabled_spouse = spouse & disabled

        return (
            spouse * p.amount.basic_credit
            + age_eligible_spouse * p.age.age_credit
            + disabled_spouse * p.amount.disability_credit
        )
