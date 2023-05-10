from policyengine_canada.model_api import *


class ns_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.ns.tax.income.credits.refundable"
