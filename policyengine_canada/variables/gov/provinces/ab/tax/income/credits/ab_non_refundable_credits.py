from policyengine_canada.model_api import *


class ab_non_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "Alberta non-refundable credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB
    adds = "gov.provinces.ab.tax.income.credits.non_refundable"
