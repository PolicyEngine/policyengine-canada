from policyengine_canada.model_api import *


class nu_eligible_dependent_credit_eligible(Variable):
    value_type = float
    entity = Person
    label = "Eligible for the Nunavut eligible dependent credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nu.tax.income.credits.eligible_dependent_credit
        spouse = person("is_spouse", period)
        dependent = person("is_dependant", period)
        return ~spouse & dependent

