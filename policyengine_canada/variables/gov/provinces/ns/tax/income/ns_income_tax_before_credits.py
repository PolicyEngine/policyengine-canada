from policyengine_canada.model_api import *


class ns_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_nova_scotia = province == province.possible_values.NOVA_SCOTIA
        income = person("ns_taxable_income", period)
        p = parameters(period).gov.provinces.ns.tax.income.rate
        return in_nova_scotia * p.calc(income)
