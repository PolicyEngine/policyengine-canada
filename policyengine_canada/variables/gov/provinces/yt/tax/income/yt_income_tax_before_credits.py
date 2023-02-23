from policyengine_canada.model_api import *


class yt_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Yukon income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        income = person("yt_taxable_income", period)
        p = parameters(period).gov.provinces.yt.tax.income.rate
        return p.calc(income)
