from policyengine_canada.model_api import *


class canada_workers_benefit_phase_out(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit phase out"
    definition_period = YEAR

    def formula(household, period, parameters):
        