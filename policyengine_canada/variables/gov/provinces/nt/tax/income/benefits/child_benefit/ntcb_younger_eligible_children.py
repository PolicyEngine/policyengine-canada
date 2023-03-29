from policyengine_canada.model_api import *


class ntcb_younger_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Eligible children for the NTCB in the younger bracket"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    adds = ["ntcb_younger_eligible_child"]
