from policyengine_canada.model_api import *


class sk_afb_disabled_children(Variable):
    value_type = int
    entity = Household
    label = "Sasktachewan Active Family Benefit eligible Children"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    adds = ["sk_afb_disabled_children"]
