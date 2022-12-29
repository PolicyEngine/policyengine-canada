from policyengine_canada.model_api import *


class on_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Ontario income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        income = person("on_taxable_income", period)
        p = parameters(period).gov.provinces.on.tax.income.rate
        return in_ontario * p.calc(income)
