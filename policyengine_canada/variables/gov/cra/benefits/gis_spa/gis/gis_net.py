from policyengine_canada.model_api import *

class gis_net(Variable):
    value_type = float
    entity = Person
    label = "Net Guaranteed Income Supplement"
    unit = CAD
    documentation = "Highest GIS a person is eligible for, minus their reduction. "
    definition_period = YEAR

    def formula(person, period, parameters):
        gis_cap = person("gis_cap", period)
        gis_reduction = person("gis_reduction", period)
        
        return(max(gis_cap - gis_reduction, 0))


     
