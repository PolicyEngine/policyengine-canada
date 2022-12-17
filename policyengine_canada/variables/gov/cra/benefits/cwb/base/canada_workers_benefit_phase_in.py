from policyengine_canada.model_api import *


class canada_workers_benefit_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit phase in"
    definition_period = YEAR

    def formula(household, period, parameters):
        