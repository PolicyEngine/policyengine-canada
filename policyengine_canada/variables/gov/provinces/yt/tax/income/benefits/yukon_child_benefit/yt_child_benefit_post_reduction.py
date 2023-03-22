from policyengine_canada.model_api import *


class yt_child_benefit_post_reduction(Variable):
    value_type = bool
    entity = Household
    label = "Yukon child benefit post reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.YT
