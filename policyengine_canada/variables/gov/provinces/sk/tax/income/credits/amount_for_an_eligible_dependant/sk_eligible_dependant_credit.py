from policyengine_canada.model_api import *


class sk_eligible_dependant_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan eligible dependant credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.amount_for_an_eligible_dependant

        dependant_income = person("dependant_income", period)
        live_together = person("joint_living", period)
        spouse = person("is_spouse", period)
        support = person("is_supportive", period)
        spouse_eligible = (~spouse) | (spouse & ~live_together & ~support)
        dependant = person("is_dependant", period)
        live_with_dependant = live_together & dependant
        is_related = person("is_relative", period)
        dependant_eligible = live_with_dependant * is_related
        reduction = where(
            dependant_income <= p.net_income_base_amount, 0, dependant_income
        )
        reduced_amount = p.maximum_amount - reduction

        return spouse_eligible * dependant_eligible * max_(0, reduced_amount)
