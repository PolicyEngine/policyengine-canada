from policyengine_canada.model_api import *


class qc_fa_payment_two_parent(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance payment amount for two parent family"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("count_children", period)
        spouse = household("is_married", period)

        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.fa.amount.two_parent_family

        return spouse * (
            select(
                # number of children.
                [
                    children == 1,
                    children == 2,
                    children == 3,
                    children == 4,
                    children == 5,
                ],
                # payment amount
                [
                    p.one_child.calc(income),
                    p.two_children.calc(income),
                    p.three_children.calc(income),
                    p.four_children.calc(income),
                    p.five_children.calc(income),
                ],
                default=0,
            )
        )
