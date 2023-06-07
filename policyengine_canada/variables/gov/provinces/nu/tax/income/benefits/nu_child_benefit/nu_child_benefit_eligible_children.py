from policyengine_canada.model_api import *


class nu_child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Nunvaut child benefit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    adds = ["nu_child_benefit_eligible_child"]
