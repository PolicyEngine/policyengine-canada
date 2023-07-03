from policyengine_canada.model_api import *


class qc_adapted_work_premium_single_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec adapted work premium tax credit for singles"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.adapted_work_premium

        meet_requirement = household("qc_work_premium_requirements", period)

        # family situation
        single = ~household("is_married", period)
        had_child = household("count_children", period) > 0

        family_income_limit = where(
            had_child,
            p.single.single_parent.family_income_limit,
            p.single.person_living_alone.family_income_limit,
        )
        income = household("adjusted_family_net_income", period)
        family_income_eligible = income < family_income_limit

        # personal situation
        person = household.members
        disabled = person("is_disabled", period)

        work_income = person("working_income", period)
        work_income_eligible = work_income > p.work_income_limit

        eligible = (
            disabled
            & meet_requirement
            & work_income_eligible
            & family_income_eligible
        )

        # supplement
        supplement = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.supplement
        supplement_eligible = work_income > supplement.work_income_eligibility
        supplement_amount = supplement_eligible * supplement.single_amount

        # credit amount
        basic_amount = where(
            had_child,
            p.single.single_parent.amount,
            p.single.person_living_alone.amount,
        )

        return eligible * max_(
            0, basic_amount + supplement_amount - p.reduction.calc(income)
        )
