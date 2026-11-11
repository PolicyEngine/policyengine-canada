from policyengine_canada.model_api import *


class child_care_expense_deduction(Variable):
    value_type = float
    entity = Household
    label = "Child care expense deduction"
    documentation = "Federal deduction for child care expenses (line 21400). In two-parent households, typically claimed by the lower-income spouse."
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t778/t778-24e.pdf",
    )

    def formula(household, period, parameters):
        person = household.members

        # Step 1: Cap each child's expenses at their per-child maximum
        expenses = person("childcare_expense", period)
        max_per_child = person("child_care_expense_deduction_max_per_child", period)
        capped_expenses = min_(expenses, max_per_child)
        total_household_expenses = household.sum(capped_expenses)

        # Step 2: Apply 2/3 earned income limit per ITA s. 63(1)(e)
        # "2/3 of the taxpayer's earned income" - the taxpayer is the
        # lower-income claimant per ITA s. 63(2), not the family total.
        p = parameters(period).gov.cra.deductions.child_care_expense

        is_claimant = person("is_child_care_expense_claimant", period)

        # Claimant's earned income per ITA s. 63(3)
        # ITA s. 63(3) "earned income" also includes CPP/QPP disability
        # benefits, taxable scholarships/fellowships/bursaries,
        # apprenticeship incentive grants, and research grants (net of
        # expenses). These are not yet modeled in policyengine-canada.
        person_earned_income = person("employment_income", period) + person(
            "self_employment_income", period
        )
        claimant_earned_income = household.sum(
            where(is_claimant, person_earned_income, 0)
        )
        earned_income_limit = claimant_earned_income * p.earned_income_fraction

        # Prevent negative deduction when self-employment losses
        # make earned_income_limit negative (ITA s. 63).
        return max_(0, min_(total_household_expenses, earned_income_limit))
