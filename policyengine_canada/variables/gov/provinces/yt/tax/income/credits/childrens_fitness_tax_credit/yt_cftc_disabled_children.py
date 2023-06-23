from policyengine_canada.model_api import *


class yt_cftc_disabled_children(Variable):
    value_type = int
    entity = Household
    label = "Yukon Fitness Tax Credit Disabled Children"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    adds = ["yt_cftc_disabled_child"]
