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
        ).gov.cra.tax.income.credits.canada_employment_amount.max_amount

        employment_income = person("employment_income", period)
        other_employment_income = person("other_employment_income", period)
        total_income = employment_income + other_employment_income

        return min_(total_income, max_amount)
