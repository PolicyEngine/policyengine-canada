from policyengine_canada.model_api import *


class sk_head_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan head of household eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        household = person.household
        live_together = household("joint_living", period)
        spouse = person("is_spouse", period)
        support = person("is_supportive", period)

        return (~spouse) | (spouse & ~live_together & ~support)
