from policyengine_canada.model_api import *


class mb_spouse_credit_amount(Variable):
    value_type = float
    entity = Household
    label = "Manitoba spouse and common-law partner amoount"
    definition_period = YEAR
    defined_for = "mb_spouse_credit_eligible"

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.spouse_or_common_law_partner_amount

        spouse_income = person("spouse_income", period)

        return max_(0, p.base - spouse_income)
