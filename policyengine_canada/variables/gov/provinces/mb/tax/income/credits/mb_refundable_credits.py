from policyengine_canada.model_api import *


class mb_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "Manitoba refundable tax credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB
    adds = "gov.provinces.mb.tax.income.credits.refundable"
