from policyengine_canada.model_api import *


class mb_spouse_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba spouse and commonlaw partner net income"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):

        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.spouse_or_common_law_partner_amount

        caregiver = person("is_caregiver", period)

        spouse_income = person("spouse_income", period)

        spouse_credit_amount = (
            caregiver
            * person("mb_spouse_eligibility", period)
            * (p.base_amount - spouse_income)
        )

        return spouse_credit_amount
