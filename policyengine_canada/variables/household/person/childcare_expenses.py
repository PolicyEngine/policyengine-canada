from policyengine_canada.model_api import *


class childcare_expenses(Variable):
    value_type = float
    entity = Person
    label = "Childcare Expenses"
    unit = CAD
    documentation = "Childcare expenses that quality for the tax credit"
    definition_period = YEAR
