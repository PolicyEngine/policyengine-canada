from policyengine_canada.model_api import *


class nu_age_amount_credit_eligible_person(Variable):
    value_type = bool
    entity = Person
    label = "Nunvaut age amount credit eligible person"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            >= parameters(
                period
            ).gov.provinces.nu.tax.income.credits.age_amount.eligible_age
        )
