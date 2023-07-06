from policyengine_canada.model_api import *


class nb_benefits(Variable):
    value_type = float
    entity = Household
    label = "New Brunswick benefits"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NB
    adds = "gov.provinces.nb.benefits.benefits"
