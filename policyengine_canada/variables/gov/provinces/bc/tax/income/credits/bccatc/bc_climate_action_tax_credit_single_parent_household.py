from policyengine_canada.model_api import *


class bc_climate_action_tax_credit_single_parent_household(Variable):
    value_type = bool
    entity = Household
    label = "British Columbia Climate Action single parent status"
    unit = CAD
    documentation = "Determination wether the filer is a single parent eligible for the climate action tax credit"
    definition_period = YEAR

    def formula(household, period, parameters):
        married = household("is_married", period)
        bccatc_children = household(
            "bc_climate_action_tax_credit_dependent_children", period
        )
        return ~married & (bccatc_children > 0)
