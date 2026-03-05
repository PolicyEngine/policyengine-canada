from policyengine_canada.model_api import *


class is_child_care_expense_claimant(Variable):
    value_type = bool
    entity = Person
    label = "Whether this person is the child care expense claimant"
    documentation = "Per ITA s. 63(2), the lower net income supporting person claims the child care expense deduction. Uses total_individual_pre_tax_income as a proxy for net income to avoid circular dependency."
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t778/t778-24e.pdf",
    )

    def formula(person, period, parameters):
        household = person.household

        # Per ITA s. 63(2), the lower net income supporting person claims.
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
        return is_lowest_earner & (person_idx == min_idx_among_lowest)
