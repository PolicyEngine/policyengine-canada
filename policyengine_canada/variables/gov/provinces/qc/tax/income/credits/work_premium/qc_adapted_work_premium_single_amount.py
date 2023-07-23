from policyengine_canada.model_api import *


class qc_adapted_work_premium_single_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec adapted work premium tax credit for singles filers"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.adapted_work_premium

        meet_requirement = household("qc_work_premium_eligibility", period)

        # family situation
        single = ~household("is_married", period)
        has_child = household("count_children", period) > 0

        income = household("adjusted_family_net_income", period)

        # work income eligibility
        work_income_eligible = (
            household("family_working_income", period) > p.work_income_limit
        )

        eligible = meet_requirement & work_income_eligible & single

        # credit amount
        credit = where(
            has_child,
            p.single.amount.single_parent,
            p.single.amount.person_living_alone,
        )

        return eligible * max_(0, credit - p.single.reduction.calc(income))
