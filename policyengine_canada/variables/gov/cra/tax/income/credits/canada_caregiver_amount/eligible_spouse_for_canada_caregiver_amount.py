from policyengine_canada.model_api import *


class eligible_spouse_for_canada_caregiver_amount(Variable):
    value_type = bool
    entity = Person
    label = "Spouse eligible for the Canada caregiver amount"
    definition_period = YEAR

    def formula(person, period, parameters):
        disabled = person("is_disabled", period)
        spouse = person("is_spouse", period)
        return disabled & spouse
