from policyengine_canada.model_api import *


class on_child_care_fee_subsidy_full_time(Variable):
    value_type = float
    entity = Person
    label = "Ontario Child Care Fee Subsidy in full time care"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        childcare_expenses = person("childcare_costs", period)
        days = person("childcare_received_days", period)
        factor = parameters(
            period
        ).gov.provinces.on.subsidies.on_child_care_fee_subsidy.part_time_child_care_multiplication_factor
        return (childcare_expenses / (days * factor)) * days
