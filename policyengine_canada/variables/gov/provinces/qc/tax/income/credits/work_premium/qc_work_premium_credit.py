from policyengine_canada.model_api import *


class qc_work_premium_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec work premium tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        qc_work_premium_single_amount = household(
            "qc_work_premium_single_amount", period
        )
        qc_work_premium_couple_amount = household(
            "qc_work_premium_couple_amount", period
        )
        qc_adapted_work_premium_single_amount = household(
            "qc_adapted_work_premium_single_amount", period
        )
        qc_adapted_work_premium_couple_amount = household(
            "qc_adapted_work_premium_couple_amount", period
        )

        # If you are entitled to both the work premium and the adapted work premium, you will receive the greater of the two
        single_amount = max_(
            qc_work_premium_single_amount,
            qc_adapted_work_premium_single_amount,
        )

        couple_amount = max_(
            qc_work_premium_couple_amount,
            qc_adapted_work_premium_couple_amount,
        )

        supplement = household("qc_work_premium_supplement_amount", period)

        return single_amount + couple_amount + supplement
