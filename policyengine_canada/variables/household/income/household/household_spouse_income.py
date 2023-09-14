from policyengine_canada.model_api import *


class household_spouse_income(Variable):
    value_type = int
    entity = Household
    label = "Household spouse income"
    unit = CAD
    documentation = "Spouse's Individual Net Income on the household level"
    definition_period = YEAR

    adds = ["spouse_income"]
