from policyengine_canada.model_api import *


class child_care_expense_deduction_max_per_child(Variable):
    value_type = float
    entity = Person
    label = "Maximum child care expense deduction per child"
    documentation = "Maximum deductible child care expenses per eligible child based on age and disability status"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-21400-child-care-expenses.html"

    def formula(person, period, parameters):
        age = person("age", period)
        is_disabled = person("is_disabled", period)
        is_eligible = person(
            "is_eligible_child_for_child_care_expense_deduction", period
        )
        p = parameters(period).gov.cra.deductions.child_care_expense

        # Different limits based on age and disability
        # $11,000 for children with disabilities (any age)
        # $8,000 for children under 7
        # $5,000 for children 7-16

        return where(
            is_eligible,
            where(
                is_disabled,
                p.limit.disabled,
                where(
                    age < p.limit.age_threshold,
                    p.limit.under_7,
                    p.limit.over_7,
                ),
            ),
            0,
        )
