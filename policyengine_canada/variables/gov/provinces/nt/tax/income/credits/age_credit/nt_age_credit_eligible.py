from policyengine_canada.model_api import *


class nt_age_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Northwest Territories age credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.justice.gov.nt.ca/en/files/legislation/income-tax/income-tax.a.pdf#page=31"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nt.tax.income.credits.age_credit
        age = person("age", period)
        return age >= p.age_eligibility
