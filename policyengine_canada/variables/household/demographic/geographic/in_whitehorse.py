from policyengine_canada.model_api import *


class in_whitehorse(Variable):
    value_type = bool
    entity = Household
    label = "Household that resides in Whitehorse"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.YT
