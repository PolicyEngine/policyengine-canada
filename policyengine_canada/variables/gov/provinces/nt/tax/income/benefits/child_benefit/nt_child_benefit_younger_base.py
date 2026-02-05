from policyengine_canada.model_api import *


class nt_child_benefit_younger_base(Variable):
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
        return (
            (p.calc(children) * (children > 0))
            + (p.calc(children) * (children > 1))
            + (p.calc(children) * (children > 2))
            + (p.calc(children) * (children > 3))
            + (p.calc(children) * max_(children - 4, 0))
        )
