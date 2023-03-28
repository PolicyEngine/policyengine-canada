from policyengine_canada.model_api import *


class slic_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Sasktachewan low income tax credit eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    adds = ["slic_eligible_child"]
