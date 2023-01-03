from policyengine_canada.model_api import *


class household_market_income(Variable):
    value_type = float
    entity = Household
    label = "market income"
    unit = CAD
    definition_period = YEAR
    adds = ["total_individual_pre_tax_income"]
