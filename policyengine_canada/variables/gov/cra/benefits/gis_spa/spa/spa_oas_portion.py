from policyengine_canada.model_api import *


class spa_oas_portion(Variable):
    value_type = float
    entity = Person
    label = "Spousal Allowance OAS-equivalence portion"
    unit = CAD
    documentation = "The 'OAS-portion' of the SPA program."
    definition_period = YEAR

    def formula(person, period, parameters):
        spa_eligible = person("spa_eligible", period)
        base_amount = parameters(
            period
        ).gov.cra.benefits.gis_spa.spa_cap.oas_portion

        return base_amount * spa_eligible
