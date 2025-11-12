from policyengine_canada.model_api import *


class child_care_expense_deduction_person(Variable):
    value_type = float
    entity = Person
    label = "Child care expense deduction (person-level)"
    documentation = "Federal child care expense deduction allocated to the person in the household. In two-parent households, typically allocated to the lower-income spouse."
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-21400-child-care-expenses.html"

    def formula(person, period, parameters):
        # Get the household-level deduction
        household = person.household
        household_deduction = household("child_care_expense_deduction", period)

        # Simplified allocation: give it to the person with the lowest employment income
        # who has positive employment income in the household
        employment_income = person("employment_income", period)

        # Check if this person has the minimum employment income in the household
        min_employment_income = household.min(
            where(employment_income > 0, employment_income, inf)
        )

        is_claimant = employment_income == min_employment_income

        # Only one person per household should claim it
        return where(is_claimant, household_deduction, 0)
