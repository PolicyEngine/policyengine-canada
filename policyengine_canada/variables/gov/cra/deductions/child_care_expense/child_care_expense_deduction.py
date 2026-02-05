from policyengine_canada.model_api import *


class child_care_expense_deduction(Variable):
    value_type = float
    entity = Household
    label = "Child care expense deduction"
    documentation = "Federal deduction for child care expenses (line 21400). In two-parent households, typically claimed by the lower-income spouse."
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-21400-child-care-expenses.html"

    def formula(household, period, parameters):
        # Get household members
        person = household.members

        # Get childcare expenses and maximums for all members
        expenses = person("childcare_expense", period)
        max_per_child = person(
            "child_care_expense_deduction_max_per_child", period
        )

        # Cap each child's expenses at their maximum
        capped_expenses = min_(expenses, max_per_child)

        # Sum capped expenses to household level
        total_household_expenses = household.sum(capped_expenses)

        # Apply the 2/3 earned income limit
        # Use family employment income as the base
        family_earned_income = household("family_employment_income", period)
        p = parameters(period).gov.cra.deductions.child_care_expense
        earned_income_limit = family_earned_income * p.earned_income_fraction

        # The deduction is the lesser of total expenses and 2/3 earned income
        return min_(total_household_expenses, earned_income_limit)
