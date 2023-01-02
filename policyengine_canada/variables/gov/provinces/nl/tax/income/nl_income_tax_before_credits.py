from policyengine_canada.model_api import *


class nl_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Newfoundland and Labrador income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_nl = province == province.possible_values.NEWFOUNDLAND_AND_LABRADOR
        income = person("nl_taxable_income", period)
        p = parameters(period).gov.provinces.nl.tax.income.rate
        return in_nl * p.calc(income)
