from policyengine_canada.model_api import *


class family_employment_income(Variable):
    value_type = float
    entity = Household
    label = "Family employment income"
    unit = CAD
    documentation = "Income from employment of a family"
    definition_period = YEAR

    adds = ["employment_income"]
