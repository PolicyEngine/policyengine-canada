from policyengine_canada.model_api import *


class sk_pension_income_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan pension income credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.pension_income_amount
        pension_payments = person("pension_and_savings_plan_income", period)
        max_amount = p.maximum_amount
        return min_(pension_payments, max_amount)
