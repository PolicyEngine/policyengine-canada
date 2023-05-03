from policyengine_canada.model_api import *


class cce_eligible_nondisabled_young_children(Variable):
    value_type = int
    entity = Household
    label = "Quebec childcare tax credit eligible nondisabled young children"
    definition_period = YEAR

    adds = ["cce_eligible_nondisabled_young_child"]
