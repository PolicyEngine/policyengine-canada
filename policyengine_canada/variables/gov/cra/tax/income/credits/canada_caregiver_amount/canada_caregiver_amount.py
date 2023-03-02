from policyengine_canada.model_api import *


class canada_caregiver_amount(Variable):
    value_type = float
    entity = Person
    unit = CAD
    label = "Canada caregiver amount"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.cra.tax.income.credits.canada_caregiver_amount
        base = p.base
        dependent_income = person("dependent_net_income", period)
        spouse_amount = person("spouse_or_common_law_partner_amount", period)
        dependent_amount = person("eligible_dependent_amount", period)
        max_amount = p.max_amount
        min_income = p.min_income
        eligible = (
            person("eligible_dependent_for_canada_caregiver_amount", period)
            | person("eligible_spouse_for_canada_caregiver_amount", period)
        ) & dependent_income >= min_income

        income_adjusted = min_(max_(base - dependent_income, 0), max_amount)
        return eligible * (
            max_(0, income_adjusted - (spouse_amount + dependent_amount))
        )


# TODO: integration test
