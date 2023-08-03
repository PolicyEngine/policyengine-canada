from policyengine_canada.model_api import *


class qc_fa_payment(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance payment amount"
    reference = "https://www.legisquebec.gouv.qc.ca/en/document/cs/I-3?langCont=en#se:1029_8_61_18"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        eligibility = household("count_children", period) > 0

        # check if the household has cohabiting spouse
        has_spouse = household("is_married", period)

        # check if each child is full custody
        person = household.members
        full_custody = person("full_custody", period)
        shared_custody_reduction = where(
            full_custody, full_custody, p.shared_custody_reduction
        )

        # method 1: calculate using max amount with reduction threshold, (C + D) − 4% (E − F) in taxation axt
        maximum_child_amount = household.sum(
            p.child_amount.max * shared_custody_reduction
        )

        single_parent_max_amount = where(
            has_spouse, 0, p.single_parent_amount.max
        )

        income = household("adjusted_family_net_income", period)
        reduction = where(
            has_spouse,
            p.reduction_threshold.two_parent_family.calc(income),
            p.reduction_threshold.single_parent_family.calc(income),
        )
        max_credit_amount = (
            maximum_child_amount + single_parent_max_amount - reduction
        )

        # method 2: calculate using min amounts, G+H in taxation axt
        minimum_child_amount = household.sum(
            p.child_amount.min * shared_custody_reduction
        )
        single_parent_min_amount = where(
            has_spouse, 0, p.single_parent_amount.min
        )

        min_credit_amount = minimum_child_amount + single_parent_min_amount

        return eligibility * max_(min_credit_amount, max_credit_amount)
