from policyengine_canada.model_api import *


class on_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "Ontario income tax before refundable credits"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"
    adds = ["on_income_tax_before_credits"]
