from policyengine_canada.model_api import *


class taxable_other_than_dividend_income(Variable):
    value_type = float
    entity = Household
    label = "other than dividend income"
    unit = CAD
    definition_period = YEAR
