from policyengine_canada.model_api import *


class bc_benefits(Variable):
    value_type = float
    entity = Household
    label = "BC benefits"
    documentation = "British Columbia benefits"
    unit = CAD
    definition_period = YEAR

    adds = "gov.provinces.bc.benefits.benefits"
