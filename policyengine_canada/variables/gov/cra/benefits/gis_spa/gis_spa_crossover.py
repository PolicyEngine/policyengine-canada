from policyengine_canada.model_api import *


class gis_spa_crossover(Variable):
    value_type = float
    entity = State
    label = "GIS-SPA couple crossover"
    unit = CAD
    documentation = "Corresponds to SPAXO in the SPSD/M parameter guide. This is the point at which a single GIS pensioner would receive a higher benefit than a couple with combined GIS/SPA, creating the incentive for a couple to just not apply for the SPA. See page 65 of the SPSD/M 29.0 algorithm guide."
    definition_period = YEAR

    def formula(state, period, parameters):
        breakeven_spa_eligible = state("breakeven_spa_eligible", period)
        breakeven_spa_ineligible = state("breakeven_spa_ineligible", period)

        return 2 * breakeven_spa_eligible - breakeven_spa_ineligible
