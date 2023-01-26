from policyengine_canada.model_api import *


class bc_family_benefit_first_reduction(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit first reduction"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("child_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb
        base = household("bc_family_benefit_base", period)
        reduction = base - p.first_reduction.rate.calc(income)
        return max_(
            min_(
                select(
                    # Conditions.
                    [children == 1, children == 2, children > 2],
                    # Results.
                    [
                        p.first_reduction.max_amount.one_child,
                        p.first_reduction.max_amount.two_children,
                        p.first_reduction.max_amount.three_or_more_children,
                    ],
                    default=0,
                ),
                reduction,
            ),
            0,
        )
