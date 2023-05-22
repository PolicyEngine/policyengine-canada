from policyengine_canada.model_api import *


class yt_ygcpri_spouses(Variable):
    value_type = int
    entity = Household
    label = "Yukon YGCPRI eligible spouses"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    adds = ["yt_ygcpri_spouse"]
