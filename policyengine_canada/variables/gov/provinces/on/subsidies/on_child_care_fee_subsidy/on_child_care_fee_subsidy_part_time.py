from policyengine_canada.model_api import *


class on_child_care_fee_subsidy_part_time(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Care Fee Subsidy in part time care"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        childcare_expenses = household("childcare_costs", period)
        days = household("childcare_received_days", period)
        multiplier = parameters(
            period
        ).gov.provinces.on.subsidies.on_child_care_fee_subsidy.part_time_child_care_multiplier
        eligible = days > 0
        amount_if_eligible = childcare_expenses / multiplier
        return eligible * amount_if_eligible
