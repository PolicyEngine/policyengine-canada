from policyengine_canada.model_api import *


class nt_disability_amount_self(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Disability amount for self"
    unit = CAD
    definition_period = YEAR
    defined_for = "nt_disability_amount_self_eligible"
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        household = person.household
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.disability_amount_self
        reduction_age_threshold = (
            person("age", period) < p.additional_amount.age_eligibility
        )
        total_expenses = household("childcare_costs", period)
        expense_threshold = max_(
            total_expenses - p.additional_amount.child_care_expense_cap, 0
        )
        additional_max_with_child_care = max_(
            p.additional_amount.max_amount - expense_threshold, 0
        )
        return where(
            reduction_age_threshold,
            p.base + additional_max_with_child_care,
            p.base,
        )
