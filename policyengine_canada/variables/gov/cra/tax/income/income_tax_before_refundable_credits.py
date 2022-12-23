from policyengine_canada.model_api import *


class income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "Income tax before refundable credits"
    unit = CAD
    definition_period = YEAR
    adds = ["income_tax_before_credits"]
    subtracts = ["non_refundable_tax_credits"]
