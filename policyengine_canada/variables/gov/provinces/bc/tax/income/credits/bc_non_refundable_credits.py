from policyengine_canada.model_api import *


class bc_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "British Columbia non-refundable credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    adds = "gov.provinces.bc.tax.income.credits.non_refundable"
