from policyengine_canada.model_api import *


class mb_pension_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba pension amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        pension_and_savings_income = person(
            "pension_and_savings_plan_income", period
        )
        max_amount = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.pension_amount.max_amount
        return min_(pension_and_savings_income, max_amount)
