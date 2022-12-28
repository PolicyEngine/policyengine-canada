from policyengine_canada.model_api import *


class household_net_income(Variable):
    value_type = float
    entity = Household
    label = "net income"
    unit = CAD
    definition_period = YEAR
    adds = ["market_income", "refundable_tax_credits", "benefits"]
    subtracts = ["household_income_tax_before_refundable_credits"]
