from policyengine_canada.model_api import *


class acfb_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Alberta child and family benefit eligible children"
    definition_period = YEAR

    adds = ["acfb_eligible_child"]
