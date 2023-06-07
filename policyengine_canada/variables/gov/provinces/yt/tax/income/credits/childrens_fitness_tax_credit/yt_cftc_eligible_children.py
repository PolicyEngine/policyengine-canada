from policyengine_canada.model_api import *


class yt_cftc_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Yukon Fitness Tax Credit Eligible Children"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    adds = ["yt_cftc_eligible_child"]
