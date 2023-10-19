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
        # max_amount_child - (childcare_received - threshold)
        child_credit = (person("age", period) < p.eligible_age) * max(
            0, p.max_amount_child - max(0, childcare_received - p.threshold)
        )

        return min(p.max_amount_total, p.base + child_credit)
