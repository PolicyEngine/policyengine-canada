from policyengine_canada.model_api import *


class gst_credit_base(Variable):
    value_type = float
    entity = Household
    label = "GST Credit before the boost is applied and before reduction based on family net income"
    unit = CAD
    definition_period = YEAR

    adds = ["gst_credit_person"]
