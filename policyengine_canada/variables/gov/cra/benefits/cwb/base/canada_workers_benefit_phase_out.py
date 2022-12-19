from policyengine_canada.model_api import *


class canada_workers_benefit_phase_out(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit phase out"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household.person("adjusted_net_family_income", period)
        p = parameters(period).gov.cra.benefits.cwb
        family = household.person("is_canada_workers_benefit_family", period)
        return select(
            [family, ~family],
            [
                p.phase_out.base.family.calc(income),
                p.phase_out.base.single.calc(income),
            ],
            default=0,
        )
