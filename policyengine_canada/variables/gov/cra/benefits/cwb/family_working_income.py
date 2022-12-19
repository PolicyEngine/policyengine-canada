from policyengine_canada.model_api import *


class family_working_income(Variable):
    value_type = float
    entity = Household
    label = "Family working income"
    unit = CAD
    documentation = "Income from employment and self-employment of a family"
    definition_period = YEAR

    formula = sum_of_variables("working_income")
