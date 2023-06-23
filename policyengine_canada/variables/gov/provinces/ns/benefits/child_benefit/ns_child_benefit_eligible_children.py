from policyengine_canada.model_api import *


class ns_child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Nova Scotia child benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    adds = ["ns_child_benefit_eligible_child"]
