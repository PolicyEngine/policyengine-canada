from policyengine_canada.model_api import *

class spa_gis_reduction(Variable):
    value_type = float
    entity = Person
    label = "Reduction of the Spousal Allowance GIS-equivalence portion"
    unit = CAD
    documentation = "Reduction of the 'GIS-portion' of the GIS program."
    definition_period = YEAR

    def formula(person, period, parameters):
        household = person.household
        individual_net_income = person("individual_net_income", period)
        spouse_net_income = household("spouse_net_income", period)
        p = parameters(period).gov.cra.benefits.gis_spa.spa_reduction

        return((individual_net_income + spouse_net_income) * p.spa_gis_reduction)