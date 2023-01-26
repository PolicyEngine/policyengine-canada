from policyengine_canada.model_api import *


class oeptc_energy_component(Variable):
    value_type = float
    entity = Household
    label = "OEPTC energy component"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.energy_component
        long_term_care_home = (
            household(
                "rent_paid_to_public_or_non_profit_long_term_care_home", period
            )
            * p.multiplier
        )
        reserve_home_energy_costs = household(
            "home_energy_costs_on_a_reserve", period
        )
        student_resident = (
            household("lived_in_a_student_residence", period)
            * p.student_resident_reduction
        )
        occupancy_costs = household("oeptc_occupancy_cost", period)
        uncapped = (
            long_term_care_home
            + reserve_home_energy_costs
            + occupancy_costs
            - student_resident
        )
        return min_(uncapped, p.max_amount)
