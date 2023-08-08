from policyengine_canada.model_api import *


class qc_fa_payment(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance payment amount"
    reference = "https://www.legisquebec.gouv.qc.ca/en/document/cs/I-3?langCont=en#se:1029_8_61_18"
    definition_period = YEAR
    defined_for = "qc_fa_eligibility"

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        # check if the household has cohabiting spouse
        has_spouse = household("is_married", period)

        # eligible dependent child - under 18 years of age
        person = household.members
        age_eligible = person("age", period) < p.age_eligibility

        # check if each child is full custody
        full_custody = person("full_custody", period)
        shared_custody_multiplier = where(
            full_custody, 1, p.shared_custody_multiplier
        )

        # method 1: calculate using max amount with reduction threshold
        # (C + D) − 4% (E − F) in taxation axt
        maximum_child_amount = household.sum(
            age_eligible * p.child_amount.max * shared_custody_multiplier
        )

        single_parent_max_amount = where(
            has_spouse, 0, p.single_parent_amount.max
        )

        income = household("adjusted_family_net_income", period)
        reduction = where(
            has_spouse,
            p.reduction.two_parent_family.calc(income),
            p.reduction.single_parent_family.calc(income),
        )
        max_credit_amount = (
            maximum_child_amount + single_parent_max_amount - reduction
        )

        # method 2: calculate using min amounts, G+H in taxation axt
        minimum_child_amount = household.sum(
            age_eligible * p.child_amount.min * shared_custody_multiplier
        )
        single_parent_min_amount = where(
            has_spouse, 0, p.single_parent_amount.min
        )

        min_credit_amount = minimum_child_amount + single_parent_min_amount

        return max_(min_credit_amount, max_credit_amount)
