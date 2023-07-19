from policyengine_canada.model_api import *


class yt_pension_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon Pension Amount"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.pension_income

        pension_and_savings_income = person(
            "pension_and_savings_plan_income", period
        )

        max_values = p.amount

        return min_(max_values, pension_and_savings_income)
