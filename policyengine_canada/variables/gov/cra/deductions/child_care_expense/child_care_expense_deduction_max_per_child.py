from policyengine_canada.model_api import *


class child_care_expense_deduction_max_per_child(Variable):
    value_type = float
    entity = Person
    label = "Maximum child care expense deduction per child"
    documentation = "Maximum deductible child care expenses per eligible child based on age and disability status"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-63.html",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t778/t778-24e.pdf#page=3",
    )

    def formula(person, period, parameters):
        age = person("age", period)
        is_disabled = person("is_disabled", period)
        is_eligible = person(
            "is_eligible_child_for_child_care_expense_deduction", period
        )
        p = parameters(period).gov.cra.deductions.child_care_expense

        # Per ITA s. 63(3) "annual child care expense amount"
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
