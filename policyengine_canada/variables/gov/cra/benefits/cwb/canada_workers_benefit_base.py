from policyengine_canada.model_api import *


class canada_workers_benefit_base(Variable):
    value_type = bool
    entity = Household
    label = "Canada workers benefit base amount"
    definition_period = YEAR

    def formula(household, period, parameters):
        p = parameters(period).gov.cra.benefits.cwb
        eligible_person = household.person(
            "canada_workers_benefit_eligible", period
        )
        income = household("adjusted_net_family_income", period)
