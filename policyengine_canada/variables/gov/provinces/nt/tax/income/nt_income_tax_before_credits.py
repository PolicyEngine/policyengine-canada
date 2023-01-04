from policyengine_canada.model_api import *


class nt_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_northwest_territories = (
            province == province.possible_values.NORTHWEST_TERRITORIES
        )
        income = person("nt_taxable_income", period)
        p = parameters(period).gov.provinces.nt.tax.income.rate
        return in_northwest_territories * p.calc(income)
