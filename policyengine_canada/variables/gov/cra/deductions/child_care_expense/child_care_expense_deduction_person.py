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
        is_claimant = person("is_child_care_expense_claimant", period)
        return where(is_claimant, household_deduction, 0)
