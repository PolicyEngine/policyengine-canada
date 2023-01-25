from policyengine_canada.model_api import *


class is_child_for_on_child_care_fee_subsidy_reduction(Variable):
    value_type = bool
    entity = Person
    label = "Is a child for the Ontario Child Care Fee Subsidy reduction"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        p = parameters(
            period
        ).gov.provinces.on.subsidies.on_child_care_fee_subsidy.reduction
        return age < p.age
