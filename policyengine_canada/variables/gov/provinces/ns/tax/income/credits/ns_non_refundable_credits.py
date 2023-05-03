from policyengine_canada.model_api import *


class ns_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "NS non refundable credits"
    documentation = "Nova Scotia non refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.ns.tax.income.credits.non_refundable"
