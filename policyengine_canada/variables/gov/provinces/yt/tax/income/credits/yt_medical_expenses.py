from policyengine_canada.model_api import *


class yt_medical_expense_credit(Variable):
    value_type = float
    entity = Household
    label = "Yukon Medical Expense Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.medical_expense

        claimed_medical_expenses = household("medical_expenses", period)
        net_income = household("household_net_income", period)
        medical_expenses_rate = p.rate

        applicable_amount = min_(
            p.max_amount, net_income * medical_expenses_rate
        )

        return max_(claimed_medical_expenses - applicable_amount, 0)
