from policyengine_canada.model_api import *


class sk_eligible_dependant_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan eligible dependant credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.amount_for_an_eligible_dependant

        dependant_income = person("dependant_income", period)

        head_eligible = person("sk_head_eligibility", period)

        dependant_eligible = person("sk_dependant_eligibility", period)
        reduction = where(
            dependant_income <= p.net_income_base_amount, 0, dependant_income
        )
        reduced_amount = p.maximum_amount - reduction

        return head_eligible * dependant_eligible * max_(0, reduced_amount)
