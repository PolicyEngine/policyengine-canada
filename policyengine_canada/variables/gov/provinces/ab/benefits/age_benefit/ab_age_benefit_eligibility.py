from policyengine_canada.model_api import *


class ab_age_benefit_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Alberta age benefit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            > parameters(
                period
            ).gov.provinces.ab.benefits.ab_age_benefit.eligible_age
        )
