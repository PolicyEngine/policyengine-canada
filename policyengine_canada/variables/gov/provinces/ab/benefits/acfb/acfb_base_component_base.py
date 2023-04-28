from policyengine_canada.model_api import *


class acfb_base_component_base(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit base component base amount"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.benefits.acfb.base_component.base
        eligible_children = household("acfb_eligible_children", period)
        return (
            (p.one_child * (eligible_children > 0))
            + (p.two_children * (eligible_children > 1))
            + (p.three_children * (eligible_children > 2))
            + (p.four_or_more_children * (eligible_children > 3))
        )
