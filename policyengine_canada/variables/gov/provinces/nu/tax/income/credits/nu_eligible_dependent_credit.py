from policyengine_canada.model_api import *


class nu_eligible_dependent_credit(Variable):
    value_type = float
    entity = Household
    label = "Nunavut eligible dependent credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.eligible_dependent_credit
        
        spouse = person("is_spouse", period)
        dependent = person("is_dependant", period)
        spouse_absent = ~household.any(spouse & dependent)
        income_eligible = person("nu_eligible_dependent_credit_eligible", period)
        household_eligible = household.any(income_eligible)
        income = income_eligible * person("individual_net_income", period)
        eligible_income = household.sum(income)
        max_amount = max_(0, p.amount.additional - eligible_income)
        amount = p.amount.base + max_amount
        return (
            amount
            * household_eligible
            * spouse_absent
        )
