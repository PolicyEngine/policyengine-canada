from policyengine_canada.model_api import *


class qc_fa_exceptional_care_tier2(Variable):
    value_type = bool
    entity = Person
    label = "Quebec family allowance handicapped children requiring Tier 2 exceptional care"
    reference = "https://www.rrq.gouv.qc.ca/en/enfants/enfant_handicape/seh-necessitant-soins-exceptionnels/Pages/seh-necessitant-soins-exceptionnels.aspx"
    definition_period = YEAR
    defined_for = ProvinceCode.QC
