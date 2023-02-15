from policyengine_canada.model_api import *

class spa_oas_reduction(Variable):
    value_type = float
    entity = Person
    label = "Reduction of the Spousal Allowance OAS-equivalence portion"
    unit = CAD
    documentation = "Reduction of the 'OAS-portion' of the SPA program."
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        individual_net_income = person("individual_net_income", period)
        spouse_net_income = household("spouse_net_income", period)
        p = parameters(period).gov.cra.benefits.gis_spa.spa_reduction

        return(p.spa_oas_reduction.calc(individual_net_income + spouse_net_income))