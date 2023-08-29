from policyengine_canada.model_api import *


class qc_work_premium_couple_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec general work premium tax credit for couple filers"
    definition_period = YEAR
    defined_for = "qc_work_premium_eligibility"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.general_work_premium.couple

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
            p.amount.with_children,
            p.amount.without_children,
        )

        return eligible * max_(0, credit - p.reduction.calc(income))
