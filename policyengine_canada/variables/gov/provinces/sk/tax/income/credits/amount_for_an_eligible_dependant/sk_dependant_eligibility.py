from policyengine_canada.model_api import *


class sk_dependant_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan dependant eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        household = person.household
        live_together = household("joint_living", period)
        dependant = person("is_dependant", period)
        is_related = person("is_relative", period)

        return live_together & dependant & is_related
