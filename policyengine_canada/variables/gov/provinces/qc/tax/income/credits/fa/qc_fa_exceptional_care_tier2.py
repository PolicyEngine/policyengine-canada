from policyengine_canada.model_api import *


class qc_fa_exceptional_care_tier2(Variable):
    value_type = bool
    entity = Household
    label = "Quebec family allowance handicapped children requiring exceptional care Tier2"
    definition_period = YEAR
    defined_for = ProvinceCode.QC
