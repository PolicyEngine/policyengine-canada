from policyengine_canada.model_api import *


class nu_married_status_credit(Variable):
    value_type = float
    entity = Household
    label = "Nunavut married status credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.married_status_credit
        spouse = person("is_spouse", period)
        dependent = person("is_dependant", period)
        eligible = household.any(spouse & dependent)
        income = eligible * person("individual_net_income", period)
        eligible_income = household.sum(income)
        return (
            p.base + max_(0, p.addon_max_amount - eligible_income)
        ) * eligible
