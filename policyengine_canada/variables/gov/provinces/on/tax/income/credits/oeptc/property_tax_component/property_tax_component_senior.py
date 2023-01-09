from policyengine_canada.model_api import *


class property_tax_component_senior(Variable):
    value_type = float
    entity = Household
    label = "Oeptc property tax component for seniors"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.property_tax_component
        occupany_costs = (
            household("occupancy_costs", period) * p.multiplication_factor
        )
        return min_(p.senior.initial_cap, occupany_costs) + p.senior.supplement
