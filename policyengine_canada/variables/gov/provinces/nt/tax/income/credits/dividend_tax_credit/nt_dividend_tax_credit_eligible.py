from policyengine_canada.model_api import *


class nt_dividend_tax_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Northwest Territories dividend tax credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.NT
    reference = "https://www.justice.gov.nt.ca/en/files/legislation/income-tax/income-tax.a.pdf#page=40"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.dividend_tax_credit
        return
