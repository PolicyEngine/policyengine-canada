from policyengine_canada.model_api import *


class mb_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Manitoba Child Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(household, period, parameters):
        eligible_children = household(
            "mb_child_benefit_eligible_children", period
        )
        p = parameters(period).gov.provinces.mb.benefits.mbcb
        capped_children_count = min_(eligible_children, p.max_child_count)
        # <= 6

        income = household("adjusted_family_net_income", period)
        base_amount = capped_children_count * p.base
        reduction = select(
            [
                capped_children_count == 1,
                capped_children_count == 2,
                capped_children_count == 3,
                capped_children_count == 4,
                capped_children_count == 5,
                capped_children_count >= 6,
            ],
            [
                p.reduction.one_child.calc(income),
                p.reduction.two_children.calc(income),
                p.reduction.three_children.calc(income),
                p.reduction.four_children.calc(income),
                p.reduction.five_children.calc(income),
                p.reduction.six_or_more_children.calc(income),
            ],
            default=0,
        )
        return max_(0, base_amount - reduction)
