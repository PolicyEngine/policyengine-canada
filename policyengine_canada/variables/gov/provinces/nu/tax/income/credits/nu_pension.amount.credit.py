from policyengine_canada.model_api import *


class nu_pension_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Nu pension amount credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        pension_and_savings_income = person(
            "pension_and_savings_plan_income", period
        )
        max_amount = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.pension_income_amount.base
        return min_(pension_and_savings_income, max_amount)
