from policyengine_canada.model_api import *


class nu_married_status_credit(Variable):
    value_type = float
    entity = Household
    label = "Nunavut married status credit"
    definition_period = YEAR
    defined_for = "nu_married_status_credit_eligible"

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.married_status_credit
        spouse = person("is_spouse", period)
        dependent = person("is_dependant", period)
        eligible = household.any(spouse & dependent)
        income = income_eligible * person("individual_net_income", period)
        eligible_income = household.sum(income)
        max_amount = max_(0, p.amount.additional - eligible_income)
        return p.amount.base + max_amount
        return (
            amount
        * eligible
        )
