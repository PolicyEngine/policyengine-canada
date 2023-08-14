from policyengine_canada.model_api import *


class mb_spouse_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba spouse and commonlaw partner eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.spouse_or_common_law_partner_amount

        spouse = person("is_spouse", period)
        living_together = person("lived_together", period)
        spouse_income_eligible = (
            person("spouse_income", period) < p.base_amount
        )

        spouse_eligibility = spouse & living_together & spouse_income_eligible

        return spouse_eligibility
