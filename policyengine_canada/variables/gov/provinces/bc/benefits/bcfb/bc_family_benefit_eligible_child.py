from policyengine_canada.model_api import *


class bc_family_benefit_eligible_child(Variable):
    value_type = float
    entity = Person
    label = "British Columbia family benefit eligible child"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(period).gov.provinces.bc.benefits.bcfb
        return age < p.child_ineligible_age_threshold
