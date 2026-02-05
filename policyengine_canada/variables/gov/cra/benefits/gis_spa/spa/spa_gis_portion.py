from policyengine_canada.model_api import *


class spa_gis_portion(Variable):
    value_type = float
    entity = Person
    label = "Spousal Allowance GIS-equivalence portion"
    unit = CAD
    documentation = "The 'GIS-portion' of the SPA program. Set to the value of the GIS at the married rate by default."
    definition_period = YEAR

    def formula(person, period, parameters):
        spa_eligible = person("spa_eligible", period)
        base_amount = parameters(
            period
        ).gov.cra.benefits.gis_spa.spa_cap.gis_portion

        return base_amount * spa_eligible
