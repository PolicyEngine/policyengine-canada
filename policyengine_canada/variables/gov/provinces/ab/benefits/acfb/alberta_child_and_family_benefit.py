from policyengine_canada.model_api import *


class alberta_child_and_family_benefit(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    adds = ["acfb_base_component", "acfb_working_component"]
