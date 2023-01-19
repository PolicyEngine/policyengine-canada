from policyengine_canada.model_api import *


class on_child_care_fee_subsidy_full_time(Variable):
    value_type = float
    entity = Person
    label = "Ontario Child Care Fee Subsidy in full time care"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        income = person.household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.provinces.on.subsidies.on_child_care_fee_subsidy.full_time_calculation
        return p.calc(income)
