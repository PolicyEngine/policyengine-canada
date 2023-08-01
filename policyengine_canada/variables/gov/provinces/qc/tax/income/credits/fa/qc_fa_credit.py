from policyengine_canada.model_api import *


class qc_fa_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        payment = household("qc_fa_payment", period)
        supplement = household("qc_fa_supplement", period)

        return payment + supplement
