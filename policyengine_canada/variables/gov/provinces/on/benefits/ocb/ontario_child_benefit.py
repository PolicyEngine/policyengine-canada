from policyengine_canada.model_api import *


class ontario_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Benefit"
    unit = CAD
    documentation = (
        "Non taxable amount paid monthly per children under 18 years of age. "
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        base = household("ontario_child_benefit_base", period)
        reduction = household("ontario_child_benefit_reduction", period)
        children = household("child_benefit_eligible_children", period)
        return max_(0, (base * children) - reduction)
