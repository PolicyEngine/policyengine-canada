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
        reduction = p.rate.calc(income)
        reduced_amount = max_(p.maximum_amount - reduction, 0)
        age_eligible = age >= p.age
        return age_eligible * reduced_amount
