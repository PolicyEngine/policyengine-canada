from policyengine_canada.model_api import *


class tuition_expenses(Variable):
    value_type = float
    entity = Person
    label = "Tuition Expenses"
    unit = CAD
    documentation = "Tuition expenses & Fees incurred"
    definition_period = YEAR
