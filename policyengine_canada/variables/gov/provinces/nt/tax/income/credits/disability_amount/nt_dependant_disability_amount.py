from policyengine_canada.model_api import *

class nt_dependant_disability_amount(Variable):
    value_type = float
    entity = Household
    label = "Northwest Territories Disability Amount for depenadnts"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(household, period, parameters):
        person = household.members
        p = parameters(period).gov.provinces.nt.tax.income.credits.dependant_disability_amount
        age_eligible = person("age", period) < p.age_eligibility
        disability = person("is_disabled", period)
        childcare_expenses = person("childcare_expense", period)
        dependant = person("is_dependant", period)
        eligible = disability & dependant
        base = p.base 
        expense_threshold = max_(childcare_expenses - p.child_care_expense_cap, 0)
        additional_max_with_child_care = max_(p.additional_max - expense_threshold, 0)
        amount = eligible * where(age_eligible, base + additional_max_with_child_care, base)
        return household.sum(amount)
