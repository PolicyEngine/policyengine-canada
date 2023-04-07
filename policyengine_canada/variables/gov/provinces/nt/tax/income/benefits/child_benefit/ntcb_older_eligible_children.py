from policyengine_canada.model_api import *


class ntcb_older_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Eligible children for the NTCB in the older bracket"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    adds = ["ntcb_older_eligible_child"]
