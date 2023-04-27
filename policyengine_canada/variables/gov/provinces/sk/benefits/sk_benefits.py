from policyengine_canada.model_api import *


class sk_benefits(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.SK
    adds = "gov.provinces.sk.benefits.benefits"
