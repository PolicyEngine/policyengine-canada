from policyengine_canada.model_api import *


class canada_caregiver_amount(Variable):
    value_type = bool
    entity = Person
    unit = CAD
    label = "Canada caregiver amount"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.tax.income.credits.canada_caregiver_amount.
        base = p.base
        dependent_income = person("spouse_net_income", period)

#TODO: dependent income variable

        spouse_amount = person("spouse_or_common_law_partner_amount", period)
        dependent_amount = person()

#TODO: dependent amount

        max_amount = p.max_amount
        min_income = p.income.min
        eligible = person("eligible_dependent_for_canada_caregiver_amount", period) or person("eligible_spouse_for_canada_caregiver_amount", period)
        income_adjusted = min_(max_(base - dependent_income, 0), max_amount)
        return max_(0, income_adjusted - (spouse_amount + dependent_amount))
    