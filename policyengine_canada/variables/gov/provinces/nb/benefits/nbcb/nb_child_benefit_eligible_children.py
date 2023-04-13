from policyengine_canada.model_api import *


class nb_child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "New Brunswick child benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    adds = ["nb_child_benefit_eligible_child"]
