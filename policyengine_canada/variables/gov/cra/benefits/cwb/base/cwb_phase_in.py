from policyengine_canada.model_api import *


class cwb_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit base phase in"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        income = household("family_working_income", period)
        p = parameters(period).gov.cra.benefits.cwb.phase_in.base
        family = household("is_cwb_family", period)
        eligible = person("cwb_eligible", period)
        return select(
            [eligible & family, eligible & ~family],
            [
                p.family.calc(income),
                p.single.calc(income),
            ],
            default=0,
        )
