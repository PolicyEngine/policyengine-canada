from policyengine_canada.model_api import *


class child_disability_benefit_reduction(Variable):
    value_type = float
    entity = Household
    label = "Child Disability Benefit reduction"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("child_disability_benefit_children", period)
        p = parameters(period).gov.cra.benefits.cdb.reduction
        return select(
            # Conditions.
            [children == 1, children > 1],
            # Results.
            [p.one_child.calc(income), p.two_or_more_children.calc(income)],
            default=0,
        )
