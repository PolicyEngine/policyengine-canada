from policyengine_canada.model_api import *


class is_child_for_dental_benefit(Variable):
    value_type = bool
    entity = Person
    label = "Is child eligibibe for dental benefit"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        eligible_age = parameters(
            period
        ).gov.cra.benefits.dental_benefit.max_age_eligibility
        return age < eligible_age
