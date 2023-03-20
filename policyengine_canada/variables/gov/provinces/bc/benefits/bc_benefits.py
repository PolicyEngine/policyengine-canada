from policyengine_canada.model_api import *


class bc_benefits(Variable):
    value_type = float
    entity = Household
    label = "British Columbia benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    adds = "gov.provinces.bc.benefits.benefits"
