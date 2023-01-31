from policyengine_canada.model_api import *


class bc_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "BC refundable credits"
    documentation = "British Columbia refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.province.bc.tax.income.credits.refundable"
