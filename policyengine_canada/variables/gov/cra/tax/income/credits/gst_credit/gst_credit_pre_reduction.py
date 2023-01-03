from policyengine_canada.model_api import *


class gst_credit_pre_reduction(Variable):
    value_type = float
    entity = Household
    label = "GST Credit before reduction based on family net income"
    unit = CAD
    documentation = " "
    definition_period = YEAR

    formula = sum_of_variables(["gst_credit_person"])
