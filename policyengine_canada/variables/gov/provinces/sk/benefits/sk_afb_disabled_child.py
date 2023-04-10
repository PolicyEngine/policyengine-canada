from policyengine_canada.model_api import *


class sk_afb_disabled_child(Variable):
    value_type = bool
    entity = Person
    label = "Sasktachewan Active Family Benefit disabled Child"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        child_disabled = person("is_disabled", period)
        age_eligible = (
            person("age", period)
            <= parameters(period).gov.provinces.sk.benefits.afb.age_eligibility
        )
        return child_disabled & age_eligible
