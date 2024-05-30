from policyengine_canada.model_api import *


class taxable_dividend_income(Variable):
    value_type = float
    entity = Household
    label = "dividend income"
    unit = CAD
    definition_period = YEAR
