from policyengine_canada.model_api import *


class bc_disability_credit_additional_amount(Variable):
    value_type = float
    entity = Person
    label = "British Columbia additional disability tax credit"
    unit = CAD
    definition_period = YEAR
    reference = "href: https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-d/5010-d-22e.pdf#page=1"
    defined_for = "bc_disability_credit_additional_amount_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.bc.tax.income.credits.disability
        childcare_received = person("childcare_received", period)
        additional_amount_reduction = max_(
            0, childcare_received - p.additional_amount.income_threshold
        )
        return max_(0, p.additional_amount.younger - additional_amount_reduction)
