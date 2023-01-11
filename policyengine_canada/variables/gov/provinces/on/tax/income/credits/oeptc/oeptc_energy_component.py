from policyengine_canada.model_api import *


class oeptc_energy_component(Variable):
    value_type = float
    entity = Household
    label = "Oeptc energy component"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.energy_component
        long_term_care_home = (
            person("public_or_non_profit_long_term_care_home", period)
            * p.multiplication_factor
        )
        reserve_home_energy_costs = person(
            "home_energy_costs_on_a_reserve", period
        )
        student_resident = (
            person("lived_in_a_student_residence", period)
            * p.student_resident_reduction
        )
        occupancy_costs = household("oeptc_occupancy_costs", period)
        return min_(
            p.max_amount,
            long_term_care_home
            + reserve_home_energy_costs
            + occupancy_costs
            - student_resident,
        )
