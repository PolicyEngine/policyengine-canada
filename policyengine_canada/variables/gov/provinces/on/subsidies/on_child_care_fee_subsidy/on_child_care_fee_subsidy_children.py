from policyengine_canada.model_api import *


class on_child_care_fee_subsidy_children(Variable):
    value_type = int
    entity = Person
    label = "Ontario Child Care Fee Subsidy children"
    unit = CAD
    definition_period = YEAR

    adds = ["on_child_care_fee_subsidy_child"]
