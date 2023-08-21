from policyengine_canada.model_api import *


class mb_spouse_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba spouse and common law partner amount"
    definition_period = YEAR
    defined_for = "mb_spouse_credit_eligible"

    def formula(person, period, parameters):

        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.spouse_or_common_law_partner_amount

        spouse_income = person("spouse_income", period)
        living_together = person("cohabitating_spouses", period)

        credit_amount = max_(0, (p.base - spouse_income))

        return living_together * credit_amount
