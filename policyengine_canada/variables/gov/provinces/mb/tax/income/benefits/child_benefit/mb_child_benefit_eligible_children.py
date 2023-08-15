from policyengine_canada.model_api import *


class mb_child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Manitoba child benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    adds = ["mb_child_benefit_eligible_child"]
