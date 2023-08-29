from policyengine_canada.model_api import *


class bc_climate_action_tax_credit_base(Variable):
    value_type = float
    entity = Household
    label = "British Columbia Climate Action tax Credit base amount"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    adds = ["bc_climate_action_tax_credit_person"]
