from policyengine_canada.model_api import *


class is_child_for_on_child_care_fee_subsidy(Variable):
    value_type = bool
    entity = Person
    label = "Ontario Child Care Fee Subsidy child"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.on.subsidies.on_child_care_fee_subsidy
        return age < p.child_age_eligibility
