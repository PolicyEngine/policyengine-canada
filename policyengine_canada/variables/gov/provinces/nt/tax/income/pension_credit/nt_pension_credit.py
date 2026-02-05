from policyengine_canada.model_api import *


class nt_pension_credit(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories pension credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.justice.gov.nt.ca/en/files/legislation/income-tax/income-tax.a.pdf#page=32"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.pension_credit
        federal_pension = person("pension_and_savings_plan_income", period)
        return min_(p.max_amount, federal_pension)
