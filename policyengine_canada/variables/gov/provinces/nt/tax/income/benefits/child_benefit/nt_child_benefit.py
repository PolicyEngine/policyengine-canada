from policyengine_canada.model_api import *


class nt_child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Northwest Territories Child Benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(household, period, parameters):
        younger_amount = household("nt_child_benefit_younger_base", period)
        older_amount = household("nt_child_benefit_older_base", period)
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.benefits.child_benefit
        lower_threshold = p.income_threshold.lower
        higher_threshold = p.income_threshold.higher
        income = household("adjusted_family_net_income", period)
        full_benefit_amount = younger_amount + older_amount
        # Houshold net income is required to be below #30,000 to be
        # eligible for the full benefit amount.
        full_benefit_eligibility = income <= lower_threshold
        # Houshold net income is required to be below #80,000 to be
        # eligible for the partial benefit amount.
        higher_income_eligibility = income < higher_threshold
        # The full benefit is reduced by the division of the multiplication of the
        # full benefit amount as well as the difference between the income and the
        # difference between $80,000 and $30,000.
        partial_benefit_amount = full_benefit_amount - (
            ((income - lower_threshold) * full_benefit_amount)
            / (higher_threshold - lower_threshold)
        )
        child_benefit = where(
            full_benefit_eligibility,
            full_benefit_amount,
            partial_benefit_amount,
        )
        return higher_income_eligibility * (max_(child_benefit, 0))
