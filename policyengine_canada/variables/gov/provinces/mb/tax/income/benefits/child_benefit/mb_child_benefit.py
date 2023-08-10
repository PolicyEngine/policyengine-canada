from policyengine_canada.model_api import *


class mb_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Monitoba Child Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(household, period, parameters):
        children = household("mb_child_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.mb.benefits.mbcb
        income = household("adjusted_family_net_income", period)
        base = children * p.base
        reduction = select([children == 1,
                                   children == 2,
                                   children == 3,
                                   children == 4,
                                   children == 5,
                                   children >= 6,],[
                                       p.reduction.one_child.calc(income),
                                       p.reduction.two_children.calc(income),
                                       p.reduction.three_children.calc(income),
                                       p.reduction.four_children.calc(income),
                                       p.reduction.five_children.calc(income),
                                       p.reduction.six_children.calc(income),
                                   ], default = 0,
                                   )
        return max_(0, base - reduction)
