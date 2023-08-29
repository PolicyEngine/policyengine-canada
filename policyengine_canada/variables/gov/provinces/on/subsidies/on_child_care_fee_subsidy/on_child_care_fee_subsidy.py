from policyengine_canada.model_api import *


class on_child_care_fee_subsidy(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Care Fee Subsidy"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.ONT

    def formula(household, period, parameters):
        reduction = household("on_child_care_fee_subsidy_reduction", period)
        full_time = household("full_time_childcare", period)
        full_time_care = household(
            "on_child_care_fee_subsidy_full_time", period
        )
        part_time_care = household(
            "on_child_care_fee_subsidy_part_time", period
        )
        amount_before_reduction = where(
            full_time, full_time_care, part_time_care
        )
        return max_(0, amount_before_reduction - reduction)
