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
        max_per_child = person(
            "child_care_expense_deduction_max_per_child", period
        )
        capped_expenses = min_(expenses, max_per_child)
        total_household_expenses = household.sum(capped_expenses)

        # Step 2: Apply 2/3 earned income limit per ITA s. 63(1)(e)
        # "Earned income" per ITA s. 63(3) includes employment income
        # and net self-employment income (plus scholarships, CPP/QPP
        # disability, and training allowances not yet modelled).
        family_earned_income = household.sum(
            person("employment_income", period)
            + person("self_employment_income", period)
        )
        p = parameters(period).gov.cra.deductions.child_care_expense
        earned_income_limit = family_earned_income * p.earned_income_fraction

        return min_(total_household_expenses, earned_income_limit)
