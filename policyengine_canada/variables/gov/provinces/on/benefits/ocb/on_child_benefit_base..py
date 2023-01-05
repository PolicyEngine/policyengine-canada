from policyengine_canada.model_api import *


class on_child_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Ontario Child Benefit before reduction."
    definition_period = YEAR

    def formula(household, period, parameters):
        province = household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        children = household("child_benefit_eligible_children", period)
        return in_ontario * (
            children * parameters(period).gov.provinces.on.benefits.ocb.base
        )
