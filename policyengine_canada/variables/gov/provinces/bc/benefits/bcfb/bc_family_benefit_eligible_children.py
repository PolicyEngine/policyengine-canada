from policyengine_canada.model_api import *


class bc_family_benefit_eligible_children(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit eligible children"
    unit = CAD
    definition_period = YEAR

    adds = ["bc_family_benefit_eligible_child"]
