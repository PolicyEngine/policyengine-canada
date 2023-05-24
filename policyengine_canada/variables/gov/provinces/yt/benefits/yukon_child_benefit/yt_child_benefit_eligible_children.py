from policyengine_canada.model_api import *


class yt_child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Yukon child benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    adds = ["yt_child_benefit_eligible_child"]
