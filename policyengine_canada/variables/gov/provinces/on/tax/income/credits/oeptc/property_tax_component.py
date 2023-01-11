from policyengine_canada.model_api import *


class property_tax_component(Variable):
    value_type = float
    entity = Household
    label = "Oeptc property tax component"
    unit = CAD
    definition_period = YEAR

    def formula(household, period, parameters):
        senior_status = household("oeptc_senior_status", period)
        senior = senior_status == "SENIOR"
        p = parameters(
            period
        ).gov.provinces.on.tax.income.credits.oeptc.property_tax_component
        occupany_costs = (
            household("occupancy_costs", period) * p.multiplication_factor
        )
        return where(
            senior,
            (min_(p.senior.initial_cap, occupany_costs) + p.senior.supplement),
            (
                min_(p.non_senior.initial_cap, occupany_costs)
                + p.non_senior.supplement
            ),
        )
