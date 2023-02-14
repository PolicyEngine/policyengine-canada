from policyengine_canada.model_api import *

class spa_gis_net(Variable):
    value_type = float
    entity = Person
    label = "Net GIS-portion of the SPA"
    unit = CAD
    documentation = "An individual's full GIS-portion of the SPA, minus their reduction."
    definition_period = YEAR

    def formula(person, period, parameters):
        spa_gis_portion = person("spa_gis_portion", period)
        spa_gis_reduction = person("spa_gis_reduction", period)
        
        return(max(spa_gis_portion - spa_gis_reduction, 0))


     
