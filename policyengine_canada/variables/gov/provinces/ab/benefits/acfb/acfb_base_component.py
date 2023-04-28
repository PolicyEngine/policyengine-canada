from policyengine_canada.model_api import *


class acfb_base_component(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit base component reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        reduction = household("acfb_base_component_reduction", period)
        base = household("acfb_base_component_base", period)
        return max_(0, base - reduction)
