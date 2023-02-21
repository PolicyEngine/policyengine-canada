from policyengine_canada.model_api import *


class on_child_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Ontario Child Benefit before reduction."
    definition_period = YEAR
    defined_for = ProvinceCode.ONT

    def formula(household, period, parameters):
        children = household("child_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.on.benefits.ocb
        return children * p.base
