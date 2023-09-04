from policyengine_canada.model_api import *


class household_medical_expenses(Variable):
    value_type = float
    entity = Household
    label = "Household medical expenses"
    unit = CAD
    definition_period = YEAR
