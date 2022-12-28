from policyengine_canada.model_api import *


class cwb_base_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit base phase in"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("family_working_income", period)
        p = parameters(period).gov.cra.benefits.cwb.phase_in.base
        family = household("is_cwb_family", period)
        return where(family, p.family.calc(income), p.single.calc(income))
