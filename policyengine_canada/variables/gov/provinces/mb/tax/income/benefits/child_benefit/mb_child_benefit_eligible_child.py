from policyengine_canada.model_api import *


class mb_child_benefit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba child benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.provinces.mb.benefits.mbcb
        return age < p.eligible_age
