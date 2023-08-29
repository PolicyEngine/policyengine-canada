from policyengine_canada.model_api import *


class nt_disability_amount_self(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Disability Amount for self"
    unit = CAD
    definition_period = YEAR
    defined_for = "nt_disability_amount_self_eligible"
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        household = person.household
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.disability_amount_self
        age_eligible = person("age", period) < p.age_eligibility
        total_expenses = household("childcare_costs", period)
        expense_threshold = max_(total_expenses - p.child_care_expense_cap, 0)
        additional_max_with_child_care = max_(
            p.max_additional_amount - expense_threshold, 0
        )
        return where(
            age_eligible, p.base + additional_max_with_child_care, p.base
        )
