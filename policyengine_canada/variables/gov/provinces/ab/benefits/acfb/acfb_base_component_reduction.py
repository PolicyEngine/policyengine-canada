from policyengine_canada.model_api import *


class acfb_base_component_reduction(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit base component reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.benefits.acfb.base_component.phase_out
        income = household("adjusted_family_net_income", period)
        children = household("acfb_eligible_children", period)
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
