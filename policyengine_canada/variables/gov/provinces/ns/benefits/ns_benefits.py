from policyengine_canada.model_api import *


class ns_benefits(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NS
    adds = "gov.provinces.ns.benefits.benefits"
