from policyengine_canada.model_api import *


class nu_age_amount_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the Nunavut age amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.provinces.nu.tax.income.credits.age_amount
        return age >= p.eligible_age
