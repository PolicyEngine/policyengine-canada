from policyengine_canada.model_api import *


class qc_fa_exceptional_care_tier1(Variable):
    value_type = bool
    entity = Person
    label = "Quebec family allowance handicapped children requiring exceptional care Tier1"
    definition_period = YEAR
    defined_for = ProvinceCode.QC
