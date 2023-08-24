from policyengine_canada.model_api import *


class nt_age_credit(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories age credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "nt_age_credit_eligible"
    reference = "https://www.justice.gov.nt.ca/en/files/legislation/income-tax/income-tax.a.pdf#page=31"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.nt.tax.income.credits.age_credit
        income = person("nt_taxable_income", period)
        return max_(p.max_amount - p.reduction.calc(income), 0)
