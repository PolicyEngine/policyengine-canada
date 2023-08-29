from policyengine_canada.model_api import *


class noec_count_children(Variable):
    value_type = int
    entity = Household
    label = "Northern Ontario Energy Tax Credit children"
    definition_period = YEAR

    adds = ["noec_child"]
