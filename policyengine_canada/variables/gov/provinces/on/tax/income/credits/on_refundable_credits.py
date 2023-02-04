from policyengine_canada.model_api import *


class on_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "ON refundable credits"
    documentation = "Ontario refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.on.tax.income.credits.refundable"
