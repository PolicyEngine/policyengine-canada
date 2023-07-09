from policyengine_canada.model_api import *


class sk_caregiver_amount(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan caregiver amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/td1sk/td1sk-23e.pdf"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        income = person("sk_taxable_income", period)
        p = parameters(period).gov.provinces.sk.tax.income.credits.sk_caregiver_amount
        return where(eligibility == 1, p.amount, 0)