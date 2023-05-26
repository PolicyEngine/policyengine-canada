from policyengine_canada.model_api import *


class pension_income(Variable):
    value_type = float
    entity = Person
    label = "Pension Income"
    unit = CAD
    documentation = "Income from the canada pension plan"
    definition_period = YEAR
