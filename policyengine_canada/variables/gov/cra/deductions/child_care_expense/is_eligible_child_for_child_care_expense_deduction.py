from policyengine_canada.model_api import *


class is_eligible_child_for_child_care_expense_deduction(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for child care expense deduction"
    documentation = "Whether the person is an eligible child for the federal child care expense deduction"
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t778/t778-24e.pdf#page=2",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        is_dependant = person("is_dependant", period)
        p = parameters(period).gov.cra.deductions.child_care_expense

        # Per ITA s. 63(3): child must be under 16 or have a disability
        age_eligible = age < p.age_limit
        has_disability = person("is_disabled", period)

        # Must be a dependant. Child's net income limit is not checked
        # here to avoid circular dependency (net income depends on this
        # deduction via deductions_from_total_to_net_income).
        return is_dependant & (age_eligible | has_disability)
