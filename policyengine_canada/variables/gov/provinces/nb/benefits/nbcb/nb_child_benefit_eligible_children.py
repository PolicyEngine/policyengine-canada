from policyengine_canada.model_api import *


class nb_family_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "New Brunswick family benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    adds = ["nb_family_benefit_eligible_child"]
