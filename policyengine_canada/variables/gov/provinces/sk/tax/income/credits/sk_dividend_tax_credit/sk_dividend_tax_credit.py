from policyengine_canada.model_api import *


class sk_dividend_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan Dividend Tax Credit"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5008-d/5008-d-22e.pdf#page=3"
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.dividend_tax_credit.fraction

        taxable_dividends = person("taxable_dividend_income", period)
        other_than_eligible_taxable_dividends = person(
            "tax_exempt_dividend_income", period
        )

        reduced_taxable_dividends = max_(
            taxable_dividends - other_than_eligible_taxable_dividends, 0
        )
        credits_on_eligible_taxable_dividends = (
            reduced_taxable_dividends * p.eligible
        )

        credits_on_other_than_eligible_taxable_dividends = (
            other_than_eligible_taxable_dividends * p.other_than_eligible
        )

        return (
            credits_on_eligible_taxable_dividends
            + credits_on_other_than_eligible_taxable_dividends
        )
