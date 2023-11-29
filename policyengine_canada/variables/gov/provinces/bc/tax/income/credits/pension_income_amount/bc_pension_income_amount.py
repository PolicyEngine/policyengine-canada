from policyengine_canada.model_api import *


class bc_pension_income_amount(Variable):
    value_type = float
    entity = Person
    label = "British Columbia pension income amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        pension_income = person("pension_and_savings_plan_income", period)
        max_amount = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.pension_income_amount.cap
        # Capped at a certain amount
        return min_(max_amount, pension_income)
