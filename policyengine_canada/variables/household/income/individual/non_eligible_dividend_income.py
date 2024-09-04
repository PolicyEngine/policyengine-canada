from policyengine_canada.model_api import *


class non_eligible_dividend_income(Variable):
    value_type = float
    entity = Person
    label = "Taxable Dividends (Non-Eligible)"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40425-federal-dividend-tax-credit.html"
