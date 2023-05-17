from policyengine_canada.model_api import *


class ab_age_benefit_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "New Brunswick family benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(period).gov.provinces.nb.benefits.nbcb.eligible_age
        )
