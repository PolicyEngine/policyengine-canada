from policyengine_canada.model_api import *


class ab_spouse_and_common_law_partner_amount_credit(Variable):
    value_type = float
    entity = Household
    label = "Alberta spouse and commonlaw partner amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        spouse_income = add(household, period, ["spouse_income"])
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.credits.spouse_and_common_law_partner_amount
        return max_(0, (p.base - spouse_income))
