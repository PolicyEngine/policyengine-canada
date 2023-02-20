from policyengine_canada.model_api import *


class on_benefits(Variable):
    value_type = float
    entity = Household
    label = "ON benefits"
    documentation = "Ontario benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.ON
    adds = "gov.provinces.on.benefits.benefits"
