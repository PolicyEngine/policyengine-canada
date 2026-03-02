from policyengine_canada.model_api import *


class child_care_expense_deduction_person(Variable):
    value_type = float
    entity = Person
    label = "Child care expense deduction (person-level)"
    documentation = "Federal child care expense deduction allocated to the person in the household. In two-parent households, typically allocated to the lower-income spouse."
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t778/t778-24e.pdf",
    )

    def formula(person, period, parameters):
        household = person.household
        household_deduction = household("child_care_expense_deduction", period)

        # Per ITA s. 63(2), the lower net income supporting person claims.
        # We use total_individual_pre_tax_income as a proxy for net income
        # to avoid a circular dependency (individual_net_income depends on
        # this deduction via deductions_from_total_to_net_income).
        income = person("total_individual_pre_tax_income", period)
        has_income = income > 0

        # Among earners, find the one with the lowest income.
        # Non-earners get inf so they never match the household minimum.
        earner_income = where(has_income, income, inf)
        min_earner_income = household.min(earner_income)
        is_lowest_earner = earner_income == min_earner_income

        # Use person_index as a deterministic tiebreaker when two
        # earners have equal income: lowest index claims.
        person_idx = person("person_index", period)
        min_idx_among_lowest = household.min(
            where(is_lowest_earner, person_idx, inf)
        )
        is_claimant = is_lowest_earner & (person_idx == min_idx_among_lowest)

        return where(is_claimant, household_deduction, 0)
