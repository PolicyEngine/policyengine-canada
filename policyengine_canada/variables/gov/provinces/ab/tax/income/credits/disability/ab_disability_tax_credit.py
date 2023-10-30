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
        childcare = max_(0, childcare_received - p.income_threshold)
        child_credit_eligibility = person("age", period) < p.eligible_age
        child_credit = (
            max_(0, p.max_amount.younger - childcare)
            * child_credit_eligibility
        )

        return min_(p.max_amount_total, p.max_amount.base + child_credit)
