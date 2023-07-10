from policyengine_canada.model_api import *


class qc_work_premium_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec work premium tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        person = household.members
        # check if the household has disabled member
        disabled = person("is_disabled", period)
        has_disabled_member = household.sum(disabled) > 0

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

        # assume household with disabled member would choose the credit with most beneficial
        work_premium_credit = where(
            has_disabled_member,
            max_(
                qc_work_premium_single_amount,
                qc_adapted_work_premium_single_amount,
            )
            + max_(
                qc_work_premium_couple_amount,
                qc_adapted_work_premium_couple_amount,
            ),
            qc_work_premium_single_amount + qc_work_premium_couple_amount,
        )

        supplement = household("qc_work_premium_supplement_amount", period)

        return work_premium_credit + supplement
