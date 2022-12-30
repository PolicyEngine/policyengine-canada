from policyengine_canada.model_api import *


class pe_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Prince Edward Island income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_pe = province == province.possible_values.PRINCE_EDWARD_ISLAND
        income = person("pe_taxable_income", period)
        p = parameters(period).gov.provinces.pe.tax.income.rate
        return in_pe * p.calc(income)
