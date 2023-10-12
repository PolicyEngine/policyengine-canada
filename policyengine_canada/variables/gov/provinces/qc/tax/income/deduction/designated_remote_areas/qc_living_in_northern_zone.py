from policyengine_canada.model_api import *


class qc_living_in_northern_zone(Variable):
    value_type = bool
    entity = Household
    label = "If the household live in the Northern zone of Quebec"
    definition_period = YEAR
    defined_for = ProvinceCode.QC