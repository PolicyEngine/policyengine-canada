from policyengine_canada.model_api import *


class yt_childrens_arts_credit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Yukon childrens arts credit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    adds = ["yt_childrens_arts_credit_eligible_child"]
