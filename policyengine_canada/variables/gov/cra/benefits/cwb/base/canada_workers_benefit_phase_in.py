from policyengine_canada.model_api import *


class canada_workers_benefit_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit phase in"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household.person("working_income", period)
        p = parameters(period).gov.cra.benefits.cwb
        family = household.person("is_canada_workers_benefit_family", period)
        eligible = household.person("canada_workers_benefit_eligible", period)
        return select(
            [eligible & family, eligible & ~family],
            [
                p.phase_in.base.family.calc(income),
                p.phase_in.base.single.calc(income),
            ],
            default=0,
        )
