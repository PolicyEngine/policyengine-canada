from policyengine_canada.model_api import *

class nt_disability_amount_self(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Disability Amount for self"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        household = person.household
        p = parameters(period).gov.provinces.nt.tax.income.credits.disability_amount_self
        age_eligible = person("age", period) < p.age_eligibility
        head = person("is_head", period)
        disability = person("is_disabled", period)
        eligible = head & disability
        total_expenses = household("childcare_costs", period)
        expense_threshold = max_(total_expenses - p.child_care_expense_cap, 0)
        base = p.base
        additional_max_with_child_care = max_(p.additional_max - expense_threshold, 0)
        return eligible * where(age_eligible, base + additional_max_with_child_care, base)
