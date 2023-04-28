from policyengine_canada.model_api import *


class acfb_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Alberta child and family benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.ab.benefits.acfb
        age = person("age", period)
        return age < p.age_eligibility
