from policyengine_canada.model_api import *


class breakeven_spa_eligible(Variable):
    value_type = float
    entity = State
    label = "Breakeven household income for SPA-eligible couples"
    unit = CAD
    documentation = "The level of family income at which the combination of GIS and SPA benefits have been reduced to exactly zero, which depends on the gis_spa_category of the household. We need this in order to add the 'crossover' part of the GIS reduction, as explained on page 65 of the SPSD/M Algorithm Guide. Corresponds to GISBE2 in the SPSD/M."
    definition_period = YEAR

    def formula(person, period, parameters):
        p_benefits = parameters(period).gov.cra.benefits
        p_gis_spa = p_benefits.gis_spa
        p_oas = p_benefits.old_age_security_pension
        p_oas = parameters(period).gov.cra.benefits.old_age_security_pension

        return (
            (
                (p_gis_spa.gis_cap.two_pensioners)
                / (p_gis_spa.gis_reduction.two_pensioners.rates[1])
            )
            + (
                p_oas.amount.base
                / p_gis_spa.spa_reduction.spa_oas_reduction.rates[1]
            )
            + p_gis_spa.gis_reduction.two_pensioners.thresholds[1]
        )
