from policyengine_canada.model_api import *


class spa_oas_net(Variable):
    value_type = float
    entity = Person
    label = "Net OAS-portion of the SPA"
    unit = CAD
    documentation = (
        "An individual's full OAS-portion of the SPA, minus their reduction."
    )
    definition_period = YEAR

    def formula(person, period, parameters):
        spa_oas_portion = person("spa_oas_portion", period)
        spa_oas_reduction = person("spa_oas_reduction", period)

        return max(spa_oas_portion - spa_oas_reduction, 0)
