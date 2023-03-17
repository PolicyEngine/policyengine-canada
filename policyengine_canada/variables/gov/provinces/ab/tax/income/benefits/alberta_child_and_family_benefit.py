from policyengine_canada.model_api import *


class alberta_child_and_family_benefit(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        base_component = household("base_component_post_reduction", period)
        working_component = household("working_component_post_reduction", period)
        return base_component + working_component
