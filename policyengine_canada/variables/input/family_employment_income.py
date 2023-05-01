from policyengine_canada.model_api import *

label = "Earnings"


class family_employment_income(Variable):
    value_type = float
    entity = Household
    label = "Family Employment income"
    unit = CAD
    documentation = "Income of families from gainful employment"
    definition_period = YEAR

    adds = ["employment_income"]
