from policyengine_canada.model_api import *


class qc_work_premium_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec work premium tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    adds = ["qc_work_premium_credit_base", "qc_work_premium_credit_supplement"]
