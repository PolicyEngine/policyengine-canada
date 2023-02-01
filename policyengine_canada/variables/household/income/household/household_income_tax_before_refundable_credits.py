from policyengine_canada.model_api import *


class household_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "tax"
    documentation = "Total tax liability before refundable credits."
    unit = CAD
    definition_period = YEAR
    adds = [
        "income_tax_before_refundable_credits",  # Federal.
        "on_income_tax_before_refundable_credits",  # Ontario.
        "bc_income_tax_before_refundable_credits",  # British Columbia.
    ]
