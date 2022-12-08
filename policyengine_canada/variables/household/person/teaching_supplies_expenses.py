from policyengine_canada.model_api import *


class teaching_supplies_expenses(Variable):
    value_type = float
    entity = Person
    label = "Canada expenses on teaching supplies"
    unit = CAD
    documentation = "Amount that was paid for teaching supplies"
    definition_period = YEAR
