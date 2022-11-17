from policyengine_canada.model_api import *


class child_benefit_reduction(Variable):
    value_type = float
    entity = Household
    label = "Canada Child Benefit reduction"
    unit = CAD
    documentation = (
        "Non taxable amount paid monthly per children under 18 years of age. "
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("child_benefit_eligible_children", period)
        p = parameters(period).gov.cra.benefits.ccb.reduction
        return select(
            # Conditions.
            [children == 1, children == 2, children == 3, children > 3],
            # Results.
            [
                p.one_child.calc(income),
                p.two_children.calc(income),
                p.three_children.calc(income),
                p.four_or_more_children.calc(income),
            ],
            default=0,
        )
