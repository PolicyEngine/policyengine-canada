from policyengine_canada.model_api import *


class oeptc_property_tax_component(Variable):
    value_type = float
    entity = Household
    label = "Oeptc property tax component"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        # Varies by senior status, not household type.
        senior_status = household("oeptc_senior_status", period)
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.property_tax_component
        # Step A: "Multiply the result of Step 1 by x%"
        multiplied_occupancy_cost = (
            household("occupancy_cost", period) * p.multiplication_factor
        )
        # Step B: Use A or $x, whichever is less.
        cap = p.initial_cap[senior_status]
        capped_multiplied_occupancy_cost = min_(multiplied_occupancy_cost, cap)
        # Step C: Add $x to B.
        return capped_multiplied_occupancy_cost + p.supplement[senior_status]
