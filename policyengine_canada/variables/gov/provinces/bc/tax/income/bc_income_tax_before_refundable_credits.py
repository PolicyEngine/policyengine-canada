from policyengine_canada.model_api import *


class bc_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "British Columbia income tax before refundable credits"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html"

    def formula(person, period, parameters):
        income_tax_before_credits = person(
            "bc_income_tax_before_credits", period
        )
        non_refundable_tax_credits = person(
            "bc_non_refundable_credits", period
        )
        return max_(income_tax_before_credits - non_refundable_tax_credits, 0)
