from policyengine_canada.model_api import *


class qc_cce_eligible_nondisabled_old_children(Variable):
    value_type = int
    entity = Household
    label = "Quebec childcare tax credit eligible nondisabled old children"
    definition_period = YEAR

    adds = ["qc_cce_eligible_nondisabled_old_child"]
