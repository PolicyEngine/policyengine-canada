from policyengine_canada.model_api import *


class qc_fa_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        single_parent_payment = household(
            "qc_fa_payment_single_parent", period
        )
        two_parent_payment = household("qc_fa_payment_two_parent", period)
        supplement = household("qc_fa_supplement", period)

        return single_parent_payment + two_parent_payment + supplement
