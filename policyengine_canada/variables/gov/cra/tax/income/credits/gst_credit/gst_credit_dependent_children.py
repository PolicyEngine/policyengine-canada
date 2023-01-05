from policyengine_canada.model_api import *


class gst_credit_dependent_children(Variable):
    value_type = int
    entity = Household
    label = "GST credit dependent Children"
    unit = CAD
    documentation = "Number of eligible dependent children"
    definition_period = YEAR

    formula = sum_of_variables(["is_child_for_gst_credit"])
