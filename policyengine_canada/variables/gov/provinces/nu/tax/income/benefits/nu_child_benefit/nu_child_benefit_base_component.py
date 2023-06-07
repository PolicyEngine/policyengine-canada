from policyengine_canada.model_api import *


class nu_child_benefit_base_component(Variable):
    value_type = float
    entity = Household
    label = "Nunvaut child benefit base component "
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        base = household("nu_child_benefit_base_component_base", period)
        reduction = household(
            "nu_child_benefit_base_component_reduction", period
        )
        return max_(0, base - reduction)
