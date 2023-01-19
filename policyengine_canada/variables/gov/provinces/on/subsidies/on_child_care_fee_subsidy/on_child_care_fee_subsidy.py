from policyengine_canada.model_api import *


class on_child_care_fee_subsidy(Variable):
    value_type = float
    entity = Person
    label = "Ontario Child Care Fee Subsidy"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        province = person.household("province", period)
        in_ontario = province == province.possible_values.ONTARIO
        reduction = person("on_child_care_fee_subsidy_reduction", period)
        full_time = person("full_time_childcare", period)
        full_time_care = person("on_child_care_fee_subsidy_full_time", period)
        part_time_care = person("on_child_care_fee_subsidy_part_time", period)
        return max_(
            0,
            (
                in_ontario * where(full_time, full_time_care, part_time_care)
                - reduction
            ),
        )
