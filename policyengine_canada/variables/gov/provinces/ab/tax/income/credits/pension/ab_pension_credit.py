from policyengine_canada.model_api import *


class ab_pension_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta Pension Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ab.tax.income.credits.pension
        pension_income = person("pension_and_savings_plan_income", period)
        return min_(pension_income, p.max_amount)
