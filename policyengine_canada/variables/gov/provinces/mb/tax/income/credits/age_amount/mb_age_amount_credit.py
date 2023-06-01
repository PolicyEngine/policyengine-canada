from policyengine_canada.model_api import *


class mb_age_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba age amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        age = person("age", period)
        income = person("individual_net_income", period)
        p = parameters(period).gov.provinces.mb.tax.income.credits.age_amount
        eligible = age >= p.age_eligibility
        reduced_amount = p.amount - p.reduction_rate.calc(income)
        return eligible * max_(0, reduced_amount)
