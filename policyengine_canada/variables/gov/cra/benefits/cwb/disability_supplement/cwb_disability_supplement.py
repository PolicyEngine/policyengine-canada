from policyengine_canada.model_api import *


class cwb_disability_supplement(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit disability supplement"
    definition_period = YEAR

    def formula(household, period, parameters):
        max_amount = household("cwb_disability_supplement_max_amount", period)
        phase_in = household("cwb_disability_supplement_phase_in", period)
        phase_out = household("cwb_disability_supplement_phase_out", period)
        max_amount_after_phase_in = min_(max_amount, phase_in)
        return max_(0, max_amount_after_phase_in - phase_out)
