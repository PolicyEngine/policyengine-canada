from policyengine_canada.model_api import *


class sk_dependant_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan dependant eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        live_together = person("joint_living", period)
        dependant = person("is_dependant", period)
        is_related = person("is_relative", period)
        dependant_eligible = live_together & dependant & is_related

        return dependant_eligible
