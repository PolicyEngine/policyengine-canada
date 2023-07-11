from policyengine_canada.model_api import *


class nt_age_credit(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories age credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.justice.gov.nt.ca/en/files/legislation/income-tax/income-tax.a.pdf"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nt.tax.income.credits.age_credit
        income = person("nt_taxable_income", period)
        age = person("age", period)
        eligible = age >= p.age_eligibility  # this is a bool
        return eligible * max_(p.max_amount - p.reduction.calc(income), 0)
