from policyengine_canada.model_api import *


class oshptg_adjusted_oeptc(Variable):
    value_type = float
    entity = Household
    documentation = "Ontario energy and property tax credit adjusted for the Ontario senior homeowners property tax grant"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        oshptg = person("on_senior_homeowners_property_tax_grant", period)
        eligible = oshptg > 0
        oeptc = household("oeptc", period)
        adjusted_oeptc = oshptg + oeptc
        energy_component = household("oeptc_energy_component", period)
        adjusted_for_energy_component = adjusted_oeptc - energy_component
        occupany_costs = household("oeptc_occupancy_cost", period)
        adjusted_for_occupany_costs = (
            adjusted_for_energy_component - occupany_costs
        )
        return max_(eligible * (oeptc - adjusted_for_occupany_costs), 0)
