from policyengine_canada.model_api import *


class ontario_income_tax(Variable):
    value_type = float
    entity = Person
    label = "Ontario income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"
    defined_for = Province.ONTARIO

    def formula(person, period, parameters):
        income = person("ontario_taxable_income", period)
        p = parameters(period).gov.provinces.ontario.tax
        return p.tax.calc(income)
