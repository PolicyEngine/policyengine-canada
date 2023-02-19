from policyengine_canada.model_api import *

class breakeven_spa_ineligible(Variable):
    value_type = float
    entity = State
    label = "Breakeven household income for SPA-ineligible couples"
    unit = CAD
    documentation = "The level of family income at which the combination of GIS and SPA benefits have been reduced to exactly zero, which depends on the gis_spa_category of the household. We need this in order to add the 'crossover' part of the GIS reduction, as explained on page 65 of the SPSD/M Algorithm Guide. Corresponds to GISBE1 in the SPSD/M."
    definition_period = YEAR

    def formula(person, period, parameters):
        p_gis_spa = parameters(period).gov.cra.benefits.gis_spa
        p_oas = parameters(period).gov.cra.benefits.old_age_security_pension

        return((p_gis_spa.gis_cap.one_pensioner / p_gis_spa.gis_reduction.two.pensioners[rate]) + p_oas.amount.base + p_gis_spa.gis_reduction.one.pensioner[threshold])