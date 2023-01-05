from policyengine_canada.model_api import *


class gst_credit_single_parent_household(Variable):
    value_type = bool
    entity = Household
    label = "GST Credit single parent status"
    unit = CAD
    documentation = "Determination wether the filer is a single parent eligible for the full boost amount in the GST credit."
    definition_period = YEAR

    def formula(household, period, parameters):
        married = household("is_married", period)
        gst_credit_children = household(
            "gst_credit_dependent_children", period
        )
        return ~married & (gst_credit_children > 0)
