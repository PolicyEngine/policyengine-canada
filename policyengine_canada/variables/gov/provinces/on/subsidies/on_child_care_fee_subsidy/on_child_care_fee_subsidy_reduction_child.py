from policyengine_canada.model_api import *


class on_child_care_fee_subsidy_reduction_child(Variable):
    value_type = bool
    entity = Person
    label = "Ontario Child Care Fee Subsidy reduction child"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            parameters(
                period
            ).gov.provinces.on.subsidies.on_child_care_fee_subsidy.reduction.age
            > age
        )
