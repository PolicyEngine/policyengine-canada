from policyengine_canada.model_api import *


class gis_exemption(Variable):
    value_type = float
    entity = Person
    label = "GIS Exemption"
    unit = CAD
    documentation = "Income exempt from GIS reductions"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.gis_spa.gis_exemption
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        return p.gis_exemption.calc(employment_income - self_employment_income)
