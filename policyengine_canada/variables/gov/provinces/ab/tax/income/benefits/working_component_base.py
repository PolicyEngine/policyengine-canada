from policyengine_canada.model_api import *


class working_component_base(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit working component base amount"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.benefits.acfb.working_component
        eligible_children = household("acfb_eligible_children", period)
        return select(
            [
                eligible_children == 1,
                eligible_children == 2,
                eligible_children == 3,
                eligible_children > 3,
            ],
            [
                p.one_child.base,
                p.two_children.base + p.one_child.base,
                p.three_children.base + p.two_children.base + p.one_child.base,
                p.four_or_more_children.base
                + p.three_children.base
                + p.two_children.base
                + p.one_child.base,
            ],
            default=0,
        )
