from policyengine_canada.model_api import *


class bc_family_benefit_first_reduction(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit first reduction"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("bc_family_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb.first_reduction
        base = household("bc_family_benefit_base", period)
        reduction = p.rate.calc(income)
        # The maximum family benefit is reduced to an amount dependent on the amount of children.
        # Each child has a designated amount, varying for the first two children.
        reduction_cap = (
            ((children > 0) * p.max_amount.one_child)
            + ((children > 1) * p.max_amount.two_children)
            + (max_(children - 2, 0) * p.max_amount.three_or_more_children)
        )
        return max_(max_(base - reduction, reduction_cap), 0)
