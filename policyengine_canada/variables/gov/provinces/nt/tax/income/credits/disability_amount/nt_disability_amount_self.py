from policyengine_canada.model_api import *


class nt_disability_amount_self(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories disability amount for self"
    unit = CAD
    definition_period = YEAR
    defined_for = "nt_disability_amount_self_eligible"
    reference = "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5012-d/5012-d-22e.pdf#page=2"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.disability_amount_self
        reduction_age_threshold = (
            person("age", period) < p.additional_amount.age_eligibility
        )
        total_expenses = person("care_costs_for_self", period)
        expense_reduction = max_(
            total_expenses - p.additional_amount.expense_cap, 0
        )
        additional_amount = max_(
            p.additional_amount.max_amount - expense_reduction, 0
        )
        return where(
            reduction_age_threshold,
            p.base + additional_amount,
            p.base,
        )
