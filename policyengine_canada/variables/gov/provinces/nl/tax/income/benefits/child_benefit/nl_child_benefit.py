from policyengine_canada.model_api import *


class nl_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Newfoundland and Labrador child benefit supplement"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(household, period, parameters):
        children = household("nl_child_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.nl.benefits.child_benefits
        supplement_amount = household("nl_child_benefit_supplement", period)
        benefit_amount = select(
            # Conditions.
            [children == 1, children == 2, children == 3, children >= 4],
            # Results.
            [
                p.base.one_child,
                p.base.two_children + p.base.one_child,
                p.base.three_children + p.base.two_children + p.base.one_child,
                p.base.four_children
                + p.base.three_children
                + p.base.two_children
                + p.base.one_child,
            ],
            default=0,
        )
        reduction = household("nl_child_benefit_reduction", period)
        return max_((benefit_amount - reduction), 0) + supplement_amount
