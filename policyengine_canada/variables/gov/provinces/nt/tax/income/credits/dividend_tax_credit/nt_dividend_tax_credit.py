from policyengine_canada.model_api import *


class nt_dividend_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories dividend tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "nt_dividend_tax_credit_eligible"
    reference = "https://www.justice.gov.nt.ca/en/files/legislation/income-tax/income-tax.a.pdf#page=40"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.dividend_tax_credit
        income = person("nt_taxable_income", period)
        non_eligible_dividends = B * p.noneligible_rate
        eligible_credit = (A - B) * p.taxable_rate
        return non_eligible_dividends + eligible_credit
