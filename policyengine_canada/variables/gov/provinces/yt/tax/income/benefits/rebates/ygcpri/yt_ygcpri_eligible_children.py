from policyengine_canada.model_api import *


class yt_ygcpri_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Yukon YGCPRI eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    adds = ["yt_ygcpri_eligible_child"]
