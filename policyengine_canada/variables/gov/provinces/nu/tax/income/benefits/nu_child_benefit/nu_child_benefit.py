from policyengine_canada.model_api import *


class nu_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Nunvaut child benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    adds = [
        "nu_child_benefit_base_component",
        "nu_child_benefit_working_component",
    ]
