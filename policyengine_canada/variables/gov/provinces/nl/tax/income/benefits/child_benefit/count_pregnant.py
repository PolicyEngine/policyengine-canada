from policyengine_canada.model_api import *


class count_pregnant(Variable):
    value_type = int
    entity = Household
    label = "Pregnant people in household"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    adds = ["is_pregnant"]