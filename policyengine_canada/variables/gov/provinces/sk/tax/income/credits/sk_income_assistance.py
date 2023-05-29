from policyengine_canada.model_api import *


class sk_income_assistance(Variable):
    value_type = bool
    entity = Household
    label = "Saskatchewan income assitance program"
    unit = CAD
    documentation = "whether receive support from another Government of Saskatchewan income assistance or training program"
    definition_period = YEAR
    defined_for = ProvinceCode.SK
