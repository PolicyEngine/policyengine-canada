from policyengine_canada.model_api import *


class is_eligible_child_for_child_care_expense_deduction(Variable):
    value_type = bool
    entity = Person
    label = "Eligible child for child care expense deduction"
    documentation = "Whether the person is an eligible child for the federal child care expense deduction"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-21400-child-care-expenses.html"

    def formula(person, period, parameters):
        age = person("age", period)
        is_dependant = person("is_dependant", period)
        p = parameters(period).gov.cra.deductions.child_care_expense

        # Child must be under 16 at year start OR be mentally/physically infirm
        age_eligible = age < p.age_limit

        # Or child has disability (any age)
        has_disability = person("is_disabled", period)

        # Must be a dependant (this implicitly handles the income requirement)
        # Note: We don't check child's net income here to avoid circular dependency
        # since net income depends on deductions which depend on this eligibility
        return is_dependant & (age_eligible | has_disability)
