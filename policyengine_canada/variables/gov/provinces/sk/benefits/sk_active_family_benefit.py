from policyengine_canada.model_api import *


class sk_active_family_benefit(Variable):
    value_type = float
    entity = Household
    label = "Sasktachewan Active Family Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children_nondisabled = household("sk_afb_eligible_child", period)
        children_disabled = person("sk_afb_disabled_child", period)
        if income > 60000:
            refund_money = 0
        else:
            refund_money = 150 * children_nondisabled + 200 * children_disabled
        return refund_money

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.yt.benefits.child_benefit
        income = household("adjusted_family_net_income", period)
        children = household("yt_child_benefit_eligible_children", period)
        base = household("yt_child_benefit_base", period)
        reduction = select(
            [children == 1, children > 1],
            [
                p.one_child.reduction_rate.calc(income),
                p.multiple_children.reduction_rate.calc(income),
            ],
            default=0,
        )
        return max_(0, base - reduction)
