from policyengine_canada.model_api import *


class sk_eligible_dependant_credit_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Eligibility for the Saskatchewan amount for an eligible dependant credit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        household = person.household
        live_together = household("joint_living", period)
        dependant = person("is_dependant", period)
        is_related = person("is_relative", period)
        dependant_eligible = live_together & dependant & is_related
        spouse = person("is_spouse", period)
        support = person("is_supportive", period)
        head_eligible = (~spouse) | (spouse & ~live_together & ~support)

        return dependant_eligible * head_eligible
