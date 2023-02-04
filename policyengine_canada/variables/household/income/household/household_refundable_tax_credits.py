from policyengine_canada.model_api import *


class household_refundable_tax_credits(Variable):
    value_type = float
    entity = Household
    label = "refundable tax credits"
    definition_period = YEAR
    unit = CAD
    adds = [
        "refundable_tax_credits",  # Federal.
        "on_refundable_credits",  # Ontario.
        "bc_refundable_credits",  # British Columbia.
    ]
