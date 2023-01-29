from policyengine_canada.model_api import *


class gst_credit(Variable):
    value_type = float
    entity = Household
    label = "GST Credit"
    unit = CAD
    documentation = " "
    definition_period = YEAR

    def formula(household, period, parameters):
        base_amount = household("gst_credit_base", period)
        boost = household("gst_credit_singles_boost", period)
        reduction = household("gst_credit_reduction", period)
        return max(base_amount + boost - reduction, 0)
