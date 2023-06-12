from policyengine_canada.model_api import *


class ca_employment_amount(Variable):
    value_type = float
    entity = Person
    label = "Canada Employment Amount"
    unit = CAD
    definition_period = YEAR
    # defined_for = ProvinceCode.YT
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31260-canada-employment-amount.html"

    def formula(person, period, parameters):
        maximun_return_amount = parameters(
            period
        ).gov.cra.tax.income.credits.canada_employment_amount.max_amount

        employment_income = person("employment_income", period)

        return min_(employment_income, maximun_return_amount)
