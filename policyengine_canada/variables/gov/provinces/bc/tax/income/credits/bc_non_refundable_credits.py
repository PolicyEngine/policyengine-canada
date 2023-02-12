from policyengine_canada.model_api import *


class bc_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "BC non-refundable credits"
    documentation = "British Columbia non-refundable tax credits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.bc.tax.income.credits.non_refundable"
