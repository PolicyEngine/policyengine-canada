from policyengine_canada.model_api import *


class canada_workers_benefit_base_max_amount(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit base base max amount"
    definition_period = YEAR

    def formula(household, period, parameters):
        # TODO: Add by household type.
        return parameters(period).benefit.canada_workers_benefit.max_amount
