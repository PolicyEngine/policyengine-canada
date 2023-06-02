from policyengine_canada.model_api import *


class qc_fa_payment(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance payment amount"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("count_children", period)
        spouse = household("is_married", period)

        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        # check family condition
        # family_condition = select([spouse == 1, spouse == 0], [parameters(period).gov.provinces.qc.tax.income.credits.fa.two_parent_family, parameters(period).gov.provinces.qc.tax.income.credits.fa.single_parent_family])

        return p.two_parent_family.two_children_amount.calc(income)

        # return select(
        #     # number of children.
        #     [children == 1, children == 2, children == 3, children == 4, children == 5],
        #     # Results.
        #     [
        #         family_condition.one_child_amount.calc(income),
        #         family_condition.two_children_amount.calc(income),
        #         family_condition.three_children_amount.calc(income),
        #         family_condition.four_children_amount.calc(income),
        #         family_condition.five_children_amount.calc(income)
        #     ],
        #     default=0,
        # )

        # select(
        #     [spouse == 1, spouse == 0],
        #     [
        #         select(
        #             [children == 1,children == 2,children == 3,children == 4,children == 5]
        #             [
        #                 p.two_parent_family.one_child_amount.calc(income),
        #                 p.two_parent_family.two_children_amount.calc(income),
        #                 p.two_parent_family.three_children_amount.calc(income),
        #                 p.two_parent_family.four_children_amount.calc(income),
        #                 p.two_parent_family.five_children_amount.calc(income),
        #             ]
        #         ),
        #         select(
        #             [children == 1,children == 2,children == 3,children == 4,children == 5]
        #             [
        #                 p.single_parent_family.one_child_amount.calc(income),
        #                 p.single_parent_family.two_children_amount.calc(
        #                     income
        #                 ),
        #                 p.single_parent_family.three_children_amount.calc(
        #                     income
        #                 ),
        #                 p.single_parent_family.four_children_amount.calc(
        #                     income
        #                 ),
        #                 p.single_parent_family.five_children_amount.calc(
        #                     income
        #                 ),
        #             ]
        #         ),
        #     ],
        # )


# todo: check for the path of double selection
# todo: check for how to calculate shared custoby fa payments - not 0.5