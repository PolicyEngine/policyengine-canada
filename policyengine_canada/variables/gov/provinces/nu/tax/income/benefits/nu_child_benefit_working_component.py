from policyengine_canada.model_api import *


class nu_child_benefit_base_component_base(Variable):
    value_type = float
    entity = Household
    label = "Nunvaut child benefit base component"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        children = household("nu_child_benefit_eligible_children", period)
        p = parameters(
            period
        ).gov.provinces.nu.tax.benefits.nucb.working_component
        return select(
            [children == 1, children > 1],
            [p.single_child, p.single_child + p.two_or_more_children],
            default=0,
        )


# TODO: reduction
# 30_000 income example:
# base - ((30_000 - 20_921) * rate(x))
