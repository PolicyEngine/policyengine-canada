from policyengine_canada.model_api import *


class on_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "ON non refundable credits"
    documentation = "Ontario non refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.on.tax.income.credits.non_refundable"
