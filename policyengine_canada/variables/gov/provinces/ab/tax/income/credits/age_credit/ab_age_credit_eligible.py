from policyengine_canada.model_api import *


class ab_age_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the Alberta age credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            >= parameters(
                period
            ).gov.provinces.ab.tax.income.credits.age_credit.eligible_age
        )
