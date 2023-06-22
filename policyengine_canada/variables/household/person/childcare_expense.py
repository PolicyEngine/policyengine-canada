from policyengine_canada.model_api import *


class childcare_expense(Variable):
    value_type = float
    entity = Person
    label = "Expense for child care"
    unit = CAD
    definition_period = YEAR
