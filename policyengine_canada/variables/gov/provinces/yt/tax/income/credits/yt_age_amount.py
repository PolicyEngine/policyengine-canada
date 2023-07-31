from policyengine_canada.model_api import *


class yt_age_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon age amount"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        age = person("age", period)
        p = parameters(period).gov.provinces.yt.tax.income.credits.age_amount
        # reduction = (
        #     (income > p.base_amount) * (income - p.base_amount) * p.rate
        # )
        reduction = income * p.rate
        reduced_amount = max_(p.maximum_amount - reduction, 0)
        return (age >= p.age) * (income < p.income_threshold) * reduced_amount
