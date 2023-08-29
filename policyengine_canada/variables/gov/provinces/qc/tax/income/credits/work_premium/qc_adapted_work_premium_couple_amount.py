from policyengine_canada.model_api import *


class qc_adapted_work_premium_couple_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec general work premium tax credit for couple"
    definition_period = YEAR
    defined_for = "qc_adapted_work_premium_eligibility"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.adapted_work_premium

        # family situation
        has_spouse = household("is_married", period)
        has_child = household("count_children", period) > 0

        income = household("adjusted_family_net_income", period)

        # work income eligibility
        work_income_eligible = (
            household("family_working_income", period) > p.work_income_limit
        )

        eligible = work_income_eligible & has_spouse

        # credit amount
        credit = where(
            has_child,
            p.couple.amount.with_children,
            p.couple.amount.without_children,
        )

        return eligible * max_(0, credit - p.couple.reduction.calc(income))
