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
        ).gov.provinces.sk.tax.income.credits.dividend_tax_credit

        taxable_dividends = person("taxable_dividend_income", period)
        other_than_eligible_taxable_dividends = person(
            "other_than_eligible_taxable_dividend_income", period
        )

        eligible_taxable_dividends_weight_percent = p.eligible_cal_percent
        other_than_eligible_taxable_dividends_weight_percent = (
            p.other_than_eligible_cal_percent
        )

        credits_on_eligible_taxable_dividends = (taxable_dividends - other_than_eligible_taxable_dividends) * eligible_taxable_dividends_weight_percent
        credits_on_other_than_eligible_taxable_dividends = other_than_eligible_taxable_dividends * other_than_eligible_taxable_dividends_weight_percent

        return (
            credits_on_eligible_taxable_dividends + credits_on_other_than_eligible_taxable_dividends
        )