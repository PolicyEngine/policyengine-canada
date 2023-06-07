from policyengine_canada.model_api import *


class pension_and_savings_plan_income(Variable):
    value_type = float
    entity = Person
    label = "Pension and Savings Plan Income"
    unit = CAD
    documentation = "Income from pensions and savings plans"
    definition_period = YEAR
