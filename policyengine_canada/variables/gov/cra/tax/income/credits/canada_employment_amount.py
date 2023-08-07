from policyengine_canada.model_api import *


class canada_employment_amount(Variable):
    value_type = float
    entity = Person
    label = "Canada Employment Amount"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31260-canada-employment-amount.html"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.cra.tax.income.credits.canada_employment_amount
        # While the government website states that the Canada Employment Amount is designed
        # to support workers with work-related expenses, those expenses are not part of the formula.
        countable_income = add(person, period, p.income_sources)
        return min_(countable_income, p.max_amount)
