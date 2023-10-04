from policyengine_canada.model_api import *


class qc_general_work_premium_amount(Variable):
    value_type = float
    entity = Household
    label = "Quebec general work premium tax credit amount"
    definition_period = YEAR
    defined_for = "qc_general_work_premium_eligible"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.work_premium.general_work_premium

        has_child = household("count_children", period) > 0
        married = household("is_married", period)

        # credit
        credit = select(
            [
                married & has_child,
                married & ~has_child,
                ~married & has_child,
                ~married & ~has_child,
            ],
            [
                p.couple.amount.with_children,
                p.couple.amount.without_children,
                p.single.amount.single_parent,
                p.single.amount.person_living_alone,
            ],
        )

        # reduction
        income = household("adjusted_family_net_income", period)
        reduction = where(
            married,
            p.couple.reduction.calc(income),
            p.single.reduction.calc(income),
        )

        return max_(0, credit - reduction)
