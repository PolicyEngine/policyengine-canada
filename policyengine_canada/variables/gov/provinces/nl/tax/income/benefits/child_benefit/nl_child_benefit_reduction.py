from policyengine_canada.model_api import *


class nl_child_benefit_reduction(Variable):
    value_type = float
    entity = Household
    label = "Newfoundland and Labrador child benefit reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("nl_child_benefit_eligible_children", period)
        p = parameters(
            period
        ).gov.provinces.nl.benefits.child_benefits.phase_out
        return select(
            # Conditions.
            [children == 1, children == 2, children == 3, children >= 4],
            # Results.
            [
                p.one_child.calc(income),
                p.two_children.calc(income),
                p.three_children.calc(income),
                p.four_children.calc(income),
            ],
            default=0,
        )
