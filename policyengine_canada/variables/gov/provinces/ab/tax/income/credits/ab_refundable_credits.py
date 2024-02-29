from policyengine_canada.model_api import *


class ab_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "Alberta refundable tax credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB
    adds = "gov.provinces.ab.tax.income.credits.refundable"
