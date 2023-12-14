from policyengine_canada.model_api import *


class bc_disability_credit(Variable):
    value_type = float
    entity = Person
    label = "British Columbia disability tax credit"
    unit = CAD
    definition_period = YEAR
    reference = "href: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-d/5010-d-22e.pdf#page=1"
    defined_for = "bc_disability_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.bc.tax.income.credits.disability
        additional_amount = person(
            "bc_disability_credit_additional_amount", period
        )
        return min_(p.additional_amount.max_amount, p.base + additional_amount)
