from policyengine_canada.model_api import *


class sk_spouse_or_common_law_partner_credit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan spouse or common law partner credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.spouse_or_common_law_partner_amount
        person = household.members
        spouse_income = household.sum(person("spouse_income", period))
        live_with_spouse = household("cohabitating_spouses", period)
        reduction = where(
            spouse_income <= p.reduction.income_threshold,
            p.reduction.income_threshold,
            spouse_income,
        )
        reduced_amount = max_(p.base_amount - reduction, 0)
        return live_with_spouse * reduced_amount
