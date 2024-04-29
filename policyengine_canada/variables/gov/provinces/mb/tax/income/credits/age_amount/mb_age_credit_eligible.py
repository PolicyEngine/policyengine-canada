from policyengine_canada.model_api import *


class mb_age_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba age credit eligibility"
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1mb/td1mb-22e.pdf#page=1"
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.age_amount
        age = person("age", period)
        return age >= p.age_eligibility
