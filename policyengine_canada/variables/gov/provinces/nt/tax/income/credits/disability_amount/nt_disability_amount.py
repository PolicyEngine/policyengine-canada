from policyengine_canada.model_api import *

class nt_disability_amount(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Disability Amount"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nt.tax.income.credits.disability_amount
        age = person("age", period)
        dependant = person("is_dependant", period) # is this a bool?
        total_expenses = person ("nt_childcare_expense", period) #?
        eligible = age < p.age_eligibility  # this is a bool
        return max_((eligible * ((p.max_amount - dependant * (total_expense - p.child_care_expenses)) + p.base)), p.base)
