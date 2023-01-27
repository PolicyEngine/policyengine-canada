from policyengine_canada.model_api import *


class bc_family_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit base"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        children = household("bc_family_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb.base
        province = household("province", period)
        in_bc = province == province.possible_values.BRITISH_COLUMBIA
        return in_bc * select(
            # Conditions.
            [children == 1, children == 2, children > 2],
            # Results.
            [
                p.one_child,
                (p.two_children + p.one_child),
                (p.three_or_more_children + p.one_child + p.two_children),
            ],
            default=0,
        )


# TODO: Calculate amounts for each child over 2 children
