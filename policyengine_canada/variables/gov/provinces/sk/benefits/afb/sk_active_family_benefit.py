from policyengine_canada.model_api import *


class sk_active_family_benefit(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan Active Family Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children_nondisabled = household("sk_afb_eligible_children", period)
        children_disabled = household("sk_afb_disabled_children", period)
        p = parameters(period).gov.provinces.sk.benefits.afb
        return where(
            income > p.income_threshhold,
            0,
            p.base * children_nondisabled
            + p.disabled_base * children_disabled,
        )

