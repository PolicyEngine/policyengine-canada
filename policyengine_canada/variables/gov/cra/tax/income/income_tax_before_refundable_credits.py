from policyengine_canada.model_api import *


class income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "Income tax before refundable credits"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        income_tax_before_credits = person("income_tax_before_credits", period)
        non_refundable_tax_credits = person(
            "non_refundable_tax_credits", period
        )
        return max_(income_tax_before_credits - non_refundable_tax_credits, 0)
