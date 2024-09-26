from policyengine_canada.model_api import *


class nt_child_benefit_younger_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Eligible children for the Northwest Territories Child Benefit in the younger bracket"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    adds = ["nt_child_benefit_younger_eligible_child"]
