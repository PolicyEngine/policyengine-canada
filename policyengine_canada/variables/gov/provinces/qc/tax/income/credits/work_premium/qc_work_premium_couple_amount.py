from policyengine_canada.model_api import *


class qc_work_premium_couple_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec general work premium tax credit for couple"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.general_work_premium.couple

        meet_requirement = household("qc_work_premium_eligibility", period)

        # family situation
        has_spouse = household("is_married", period)
        had_child = household("count_children", period) > 0

        income = household("adjusted_family_net_income", period)

        # work income eligibility
        work_income_eligible = (
            household("family_working_income", period) > p.work_income_limit
        )

        eligible = meet_requirement & work_income_eligible & has_spouse

        # credit amount
        credit = where(
            had_child,
            p.with_children_amount,
            p.without_children_amount,
        )

        return eligible * max_(0, credit - p.reduction.calc(income))
