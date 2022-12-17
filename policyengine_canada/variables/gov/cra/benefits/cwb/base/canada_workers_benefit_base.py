from policyengine_canada.model_api import *


class canada_workers_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit base amount"
    definition_period = YEAR

    def formula(household, period, parameters):
        max_amount = household("canada_workers_benefit_max_amount", period)
        phase_in = household("canada_workers_benefit_phase_in", period)
        phase_out = household("canada_workers_benefit_phase_out", period)
        max_amount_after_phase_in = min_(max_amount, phase_in)
        return max_(0, max_amount_after_phase_in - phase_out)
