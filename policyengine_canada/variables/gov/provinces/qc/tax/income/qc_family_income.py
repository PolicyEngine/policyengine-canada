from policyengine_canada.model_api import *


class qc_family_income(Variable):
    value_type = float
    entity = Household
    label = "Quebec family income"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.QC
    adds = ["spouse_income", "head_income"]
