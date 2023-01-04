from policyengine_canada.model_api import *


class pe_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "Prince Edward Island income tax before refundable credits"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"
    adds = ["pe_income_tax_before_credits"]
