from policyengine_canada.model_api import *


class qc_fa_payment_single_parent(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance payment amount for single parent family"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        no_spouse = ~household("is_married", period)
        children = household("count_children", period)

        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        person = household.members
        full_custody_child = person("full_custody", period)

        # number of full custody children in the household
        full_custody_children = household.sum(full_custody_child)
        full_custody_payment = no_spouse * (
            select(
                # number of children.
                [
                    full_custody_children == 1,
                    full_custody_children == 2,
                    full_custody_children == 3,
                    full_custody_children == 4,
                    full_custody_children == 5,
                ],
                # Results.
                [
                    p.amount.single_parent_family.one_child.calc(income),
                    p.amount.single_parent_family.two_children.calc(income),
                    p.amount.single_parent_family.three_children.calc(income),
                    p.amount.single_parent_family.four_children.calc(income),
                    p.amount.single_parent_family.five_children.calc(income),
                ],
                default=0,
            )
        )

        # number of shared custody children in the household
        shared_custody_children = max_(children - full_custody_children, 0)
        shared_custody_amount = select(
            # number of children.
            [
                shared_custody_children == 1,
                shared_custody_children == 2,
                shared_custody_children == 3,
                shared_custody_children == 4,
                shared_custody_children == 5,
            ],
            # Results.
            [
                p.amount.two_parent_family.one_child.calc(income),
                p.amount.two_parent_family.two_children.calc(income),
                p.amount.two_parent_family.three_children.calc(income),
                p.amount.two_parent_family.four_children.calc(income),
                p.amount.two_parent_family.five_children.calc(income),
            ],
            default=0,
        )
        shared_custody_payment = (
            p.shared_custody_reduction * no_spouse * shared_custody_amount
        )
        return shared_custody_payment + full_custody_payment


# noted: there's no instruction on how to calculate the payment for shared-custody children.
# According to the calculation tool the gorvernment provided, the amount was not the exactly half amount from the table.
# Thus, the calculation is based on the number of shared-custody children in the single-parent household but half amount from the two-parent household table.
