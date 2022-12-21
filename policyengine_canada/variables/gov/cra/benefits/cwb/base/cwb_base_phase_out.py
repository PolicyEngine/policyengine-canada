from policyengine_canada.model_api import *


class cwb_base_phase_out(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit base phase out"
    definition_period = YEAR

    def formula(household, period, parameters):
        afni = household("adjusted_family_net_income", period)
        p = parameters(period).gov.cra.benefits.cwb.phase_out.base
        family = household("is_cwb_family", period)
        return where(family, p.family.calc(afni), p.single.calc(afni))
