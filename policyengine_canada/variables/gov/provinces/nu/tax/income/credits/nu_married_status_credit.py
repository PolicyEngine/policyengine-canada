from policyengine_canada.model_api import *


class nu_marries_status_credit(Variable):
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
        eligible = age > p.age_eligibility
        base = p.base
        spouse = person("is_spouse", period)*person("is_dependent", period)
        
        