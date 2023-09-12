from policyengine_canada.model_api import *


class nl_child_benefit_supplement_children(Variable):
    value_type = int
    entity = Household
    label = "Newfoundland and Labrador child benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    adds = ["nl_child_benefit_supplement_child"]
