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
        spouse_income = person("spouse_income", period)
        live_with_spouse = household("joint_living", period) & person(
            "is_spouse", period
        )
        eligible = live_with_spouse
        reduction = where(
            spouse_income <= p.net_income_base_amount,
            p.net_income_base_amount,
            spouse_income,
        )
        reduced_amount = p.reduction.base - reduction
        return eligible * max_(0, reduced_amount)
