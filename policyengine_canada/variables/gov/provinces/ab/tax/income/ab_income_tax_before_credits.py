from policyengine_canada.model_api import *


class ab_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Alberta income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_alberta = province == province.possible_values.ALBERTA
        income = person("ab_taxable_income", period)
        p = parameters(period).gov.provinces.ab.tax.income.rate
        return in_alberta * p.calc(income)
