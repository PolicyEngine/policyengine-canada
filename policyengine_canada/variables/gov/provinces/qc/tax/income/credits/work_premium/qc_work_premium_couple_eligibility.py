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

        meet_requirement = household("qc_work_premium_requirements", period)

        # family situation
        has_spouse = household("is_married", period)
        had_child = household("count_children", period) > 0

        family_income_limit = where(
            had_child,
            p.with_children.family_income_limit,
            p.without_children.family_income_limit,
        )
        income = household("adjusted_family_net_income", period)
        family_income_eligible = income < family_income_limit

        # personal situation
        person = household.members
        nondisabled = ~person("is_disabled", period)
        no_disabled_member = household.sum(nondisabled) == 0

        work_income = person("working_income", period)
        work_income_eligible = household.sum(work_income) > p.work_income_limit

        eligible = (
            no_disabled_member
            & meet_requirement
            & work_income_eligible
            & family_income_eligible
        )

        # supplement
        supplement = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.supplement
        # check if both spouses entered the labour market
        supplement_eligible = (
            household.sum(work_income > supplement.work_income_eligibility) > 1
        )
        supplement_amount = where(
            supplement_eligible,
            supplement.couple_amount,
            supplement.single_amount,
        )

        # credit amount
        basic_amount = where(
            had_child,
            p.with_children.amount,
            p.without_children.amount,
        )

        return eligible * max_(0, amount - p.reduction.calc(income))
