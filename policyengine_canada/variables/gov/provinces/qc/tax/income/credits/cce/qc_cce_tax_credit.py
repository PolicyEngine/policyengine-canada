from policyengine_canada.model_api import *


class qc_cce_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec childcare expenses tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    adds = [
        "qc_cce_disabled_child_tax_credit",
        "qc_cce_nondisabled_child_tax_credit",
    ]
