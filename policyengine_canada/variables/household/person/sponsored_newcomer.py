from policyengine_canada.model_api import *


class sponsored_newcomer(Variable):
    value_type = bool
    entity = Household
    label = "Is household a sponsored newcomer to Canada"
    definition_period = YEAR
    defined_for = ProvinceCode.SK