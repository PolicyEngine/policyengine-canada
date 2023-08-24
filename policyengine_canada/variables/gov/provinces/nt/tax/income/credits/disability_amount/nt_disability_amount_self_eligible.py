from policyengine_canada.model_api import *

class nt_disability_amount_self_eligible(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories Disability Amount for self elligibility"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1nt/td1nt-23e.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nt.tax.income.credits.disability_amount_self
        age_eligible = person("age", period) < p.age_eligibility
        head = person("is_head", period)
        disability = person("is_disabled", period)
        eligible = head & disability
        return age_eligible * eligible