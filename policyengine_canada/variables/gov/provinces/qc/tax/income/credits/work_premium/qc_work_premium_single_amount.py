from policyengine_canada.model_api import *


class qc_work_premium_single_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec general work premium tax credit for singles"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.general_work_premium.single

        meet_requirement = household("qc_work_premium_requirements", period)

        # family situation
        single = ~household("is_married", period)
        had_child = household("count_children", period) > 0

        income = household("adjusted_family_net_income", period)

        # work income eligibility
        work_income_eligible = (
            household("family_working_income", period) > p.work_income_limit
        )

        eligible = meet_requirement & work_income_eligible & single

        # credit amount
        credit = where(
            had_child,
            p.single_parent_amount,
            p.person_living_alone_amount,
        )

        return eligible * max_(0, credit - p.reduction.calc(income))
