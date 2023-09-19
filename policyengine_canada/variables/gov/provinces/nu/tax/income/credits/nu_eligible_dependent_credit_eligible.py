from policyengine_canada.model_api import *


class nu_eligible_dependent_credit_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Eligible for the Nunavut eligible dependent credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.eligible_dependent_credit
        spouse = person("is_spouse", period)
        dependent = person("is_dependant", period)
        dependent_spouse = household.any(spouse & dependent)
        dependent_non_spouse = household.any((~spouse) & dependent)
        return (~dependent_spouse) & (dependent_non_spouse)

