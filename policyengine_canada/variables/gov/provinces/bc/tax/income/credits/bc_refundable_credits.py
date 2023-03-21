from policyengine_canada.model_api import *


class bc_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "British Columbia refundable tax credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    adds = "gov.provinces.bc.tax.income.credits.refundable"
