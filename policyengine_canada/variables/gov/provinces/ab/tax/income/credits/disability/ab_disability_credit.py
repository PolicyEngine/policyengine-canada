from policyengine_canada.model_api import *


class ab_disability_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta disability tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "ab_disability_credit_eligible"
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5009-d/5009-d-22e.pdf#page=2"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ab.tax.income.credits.disability
        additional_amount = person(
            "ab_disability_credit_additional_amount", period
        )
        uncapped_amount = p.base + additional_amount
        return min_(p.cap, uncapped_amount)
