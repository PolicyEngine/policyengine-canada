from policyengine_canada.model_api import *


class ns_child_benefit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Nova Scotia child benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.provinces.ns.benefits.child_benefit
        return age < p.age_eligibility
