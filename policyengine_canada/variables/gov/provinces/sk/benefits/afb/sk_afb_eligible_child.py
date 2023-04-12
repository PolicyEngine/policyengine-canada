from policyengine_canada.model_api import *


class sk_afb_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Sasktachewan Active Family Benefit eligible Child"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            <= parameters(period).gov.provinces.sk.benefits.afb.age_eligibility
        )
