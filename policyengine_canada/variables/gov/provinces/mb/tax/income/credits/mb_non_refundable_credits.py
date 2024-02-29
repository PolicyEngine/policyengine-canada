from policyengine_canada.model_api import *


class mb_non_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "Manitoba non-refundable credits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB
    adds = "gov.provinces.mb.tax.income.credits.non_refundable"
