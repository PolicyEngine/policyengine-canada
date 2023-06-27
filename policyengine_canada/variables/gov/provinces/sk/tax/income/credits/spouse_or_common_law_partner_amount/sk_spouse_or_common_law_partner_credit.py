from policyengine_canada.model_api import *


class sk_spouse_or_common_law_partner_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan spouse or common law partner credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.spouse_or_common_law_partner_amount
        spouse_income = person("spouse_income", period)
        live_with_spouse = person("live_together_with_spouse", period)
        eligible = live_with_spouse
        reduction = where(
            spouse_income <= p.net_income_base_amount, 0, spouse_income
        )
        return max_(0, eligible * (p.maximum_amount - reduction))
