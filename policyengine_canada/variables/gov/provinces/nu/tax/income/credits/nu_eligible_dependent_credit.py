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
        income_eligible = ~spouse & dependent
        household_eligible = household.any(income_eligible)
        eligible2 = ~household.any(spouse & dependent)
        income = income_eligible * person("individual_net_income", period)
        eligible_income = household.sum(income)
        return (
            (p.base + max_(0, p.addon_max_amount - eligible_income))
            * household_eligible
            * eligible2
        )
