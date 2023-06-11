from policyengine_canada.model_api import *


class qc_fa_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    adds = [
        "qc_fa_payment_single_parent",
        "qc_fa_payment_two_parent",
        "qc_fa_supplement",
    ]
