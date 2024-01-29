from policyengine_canada.model_api import *


class qc_living_in_intermediate_zone(Variable):
    value_type = bool
    entity = Person
    label = "If the person live in the intermidiate zone of Quebec"
    definition_period = YEAR
    defined_for = ProvinceCode.QC
