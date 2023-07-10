from policyengine_canada.model_api import *


class qc_adapted_work_premium_couple_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec general work premium tax credit for couple"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.adapted_work_premium

        meet_requirement = household("qc_work_premium_requirements", period)

        # family income eligibility
        has_spouse = household("is_married", period)
        had_child = household("count_children", period) > 0

        family_income_limit = where(
            had_child,
            p.couple.with_children.family_income_limit,
            p.couple.without_children.family_income_limit,
        )
        income = household("adjusted_family_net_income", period)
        family_income_eligible = income < family_income_limit

        # work income eligibility
        work_income_eligible = (
            household("family_working_income", period) > p.work_income_limit
        )

        eligible = (
            meet_requirement & work_income_eligible & family_income_eligible
        )

        # credit amount
        credit = where(
            had_child,
            p.couple.with_children.amount,
            p.couple.without_children.amount,
        )

        return eligible * max_(0, credit - p.couple.reduction.calc(income))
