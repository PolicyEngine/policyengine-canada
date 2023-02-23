from policyengine_canada.model_api import *


class ns_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        income = person("ns_taxable_income", period)
        p = parameters(period).gov.provinces.ns.tax.income.rate
        return p.calc(income)
