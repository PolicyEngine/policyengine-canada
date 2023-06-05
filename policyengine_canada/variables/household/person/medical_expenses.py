from policyengine_canada.model_api import *


class medical_expenses(Variable):
    value_type = float
    entity = Person
    label = "Medical Expenses"
    unit = CAD
    definition_period = YEAR
