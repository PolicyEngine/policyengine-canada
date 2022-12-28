from policyengine_canada.model_api import *


class market_income(Variable):
    value_type = float
    entity = Household
    label = "Household market (pre-tax) income"
    unit = CAD
    definition_period = YEAR
    adds = ["total_individual_pre_tax_income"]
