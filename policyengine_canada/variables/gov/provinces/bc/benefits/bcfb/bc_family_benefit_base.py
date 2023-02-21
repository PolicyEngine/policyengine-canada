from policyengine_canada.model_api import *


class bc_family_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "British Columbia family benefit base"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(household, period, parameters):
        children = household("bc_family_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb.base
        amount_if_eligible = (
            ((children > 0) * p.one_child)
            + ((children > 1) * p.two_children)
            + (max_(children - 2, 0) * p.three_or_more_children)
        )
        return amount_if_eligible
