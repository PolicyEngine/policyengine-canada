from policyengine_canada.model_api import *


class nt_chil_benefit_younger_base(Variable):
    value_type = float
    entity = Household
    label = "Base amount for all younger children under the Northwest Territories Child Benefit"
    definition_period = YEAR
    unit = CAD
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.benefits.child_benefit.younger.base
        children = household(
            "nt_child_benefit_younger_eligible_children", period
        )
        print(p.five_or_more_children * (children > 4))
        return (
            (p.one_child * (children > 0))
            + (p.two_children * (children > 1))
            + (p.three_children * (children > 2))
            + (p.four_children * (children > 3))
            + (p.five_or_more_children * max_(children - 4, 0))
        )
