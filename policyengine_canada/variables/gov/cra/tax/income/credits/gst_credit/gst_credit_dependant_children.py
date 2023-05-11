from policyengine_canada.model_api import *


class gst_credit_dependant_children(Variable):
    value_type = int
    entity = Household
    label = "GST credit dependant Children"
    unit = CAD
    documentation = "Number of eligible dependant children"
    definition_period = YEAR
    adds = ["is_child_for_gst_credit"]
