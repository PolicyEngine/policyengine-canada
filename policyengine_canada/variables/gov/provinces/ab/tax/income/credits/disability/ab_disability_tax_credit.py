from policyengine_canada.model_api import *


class ab_disability_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta disability tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = "ab_disability_tax_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ab.tax.income.credits.disability
        childcare_received = person("childcare_received", period)
        additional_amount_reduction = max_(
            0, childcare_received - p.additional_amount.income_threshold
        )
        additional_amount_eligibile = (
            person("age", period) < p.additional_amount.eligible_age
        )
        max_additional_amount = max_(
            0, p.additional_amount.younger - additional_amount_reduction
        )
        additional_amount = where(
            additional_amount_eligibile, max_additional_amount, 0
        )

        return min_(
            p.additional_amount.max_amount_total, p.base + additional_amount
        )
