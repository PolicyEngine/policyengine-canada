from policyengine_canada.model_api import *


class bc_family_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit base"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        children = household("bc_family_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb.max_amount
        return select(
            # Conditions.
            [children == 1, children == 2, children > 2],
            # Results.
            [
                p.one_child,
                p.two_children,
                p.three_or_more_children,
            ],
            default=0,
        )
