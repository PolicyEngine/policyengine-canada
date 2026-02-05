from policyengine_canada.model_api import *


class nu_eligible_dependent_credit(Variable):
    value_type = float
    entity = Household
    label = "Nunavut eligible dependent credit"
    definition_period = YEAR
    defined_for = "nu_eligible_dependent_credit_eligible"

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.eligible_dependent_credit
        
        spouse = person("is_spouse", period)
        dependent = person("is_dependant", period)
        income_eligible = (~spouse) & dependent
        income = income_eligible * person("individual_net_income", period)
        eligible_income = household.sum(income)
        max_amount = max_(0, p.amount.additional - eligible_income)
        return p.amount.base + max_amount