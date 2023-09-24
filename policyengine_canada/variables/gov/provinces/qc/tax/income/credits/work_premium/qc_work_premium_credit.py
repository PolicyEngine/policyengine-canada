from policyengine_canada.model_api import *


class qc_work_premium_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec work premium tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        qc_general_work_premium_amount = household(
            "qc_general_work_premium_amount", period
        )
        qc_adapted_work_premium_amount = household(
            "qc_adapted_work_premium_amount", period
        )

        # If you are entitled to both the work premium and the adapted work premium, you will receive the greater of the two
        credit_amount = max_(
            qc_general_work_premium_amount,
            qc_adapted_work_premium_amount,
        )

        supplement = household("qc_work_premium_supplement_amount", period)

        return credit_amount + supplement
