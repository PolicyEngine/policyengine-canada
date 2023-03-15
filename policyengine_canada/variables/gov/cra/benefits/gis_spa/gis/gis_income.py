from policyengine_canada.model_api import *

class gis_income(Variable):
    value_type = float
    entity = Person
    label = "Employment income"
    unit = CAD
    documentation = "Income after GIS income exemptions, for use in calculating a person's GIS reduction. SPSD/M 29.0 Parameter Guide pg 368: the full definition of earnings for determining GIS include wages and salaries (idiemp), less other employment expenses (idalexp), clergy residence deduction (idclergy), and non-negative self-employment earnings (idise)"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.gis_spa.gis_exemption
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period) 
        exemption = person("gis_exemption", period)
        return max(employment_income - self_employment_income - exemption, 0)


