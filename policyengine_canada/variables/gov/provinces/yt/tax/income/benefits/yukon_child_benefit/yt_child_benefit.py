from policyengine_canada.model_api import *


class yt_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Yukon child benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

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
