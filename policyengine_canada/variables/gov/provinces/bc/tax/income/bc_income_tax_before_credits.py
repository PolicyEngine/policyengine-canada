from policyengine_canada.model_api import *


class bc_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "British Columbia income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_bc = province == province.possible_values.BRITISH_COLUMBIA
        income = person("bc_taxable_income", period)
        p = parameters(period).gov.provinces.bc.tax.income.rate
        return in_bc * p.calc(income)
