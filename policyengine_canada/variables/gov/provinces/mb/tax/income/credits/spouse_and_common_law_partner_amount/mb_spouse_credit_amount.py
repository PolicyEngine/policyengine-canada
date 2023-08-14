from policyengine_canada.model_api import *


class mb_spouse_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba spouse and commonlaw partner net income"
    definition_period = YEAR
    defined_for = "mb_head_eligibility"

    def formula(person, period, parameters):

        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.spouse_or_common_law_partner_amount

        spouse_income = person("spouse_income", period)
        living_together = person("lived_together", period)

        return living_together * (max_(0, (p.base_amount - spouse_income)))
