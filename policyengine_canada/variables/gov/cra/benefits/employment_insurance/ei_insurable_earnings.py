from policyengine_canada.model_api import *


class ei_insurable_earnings(Variable):
    value_type = float
    entity = Person
    label = "Employment Insurance insurable earnings"
    definition_period = YEAR
    unit = CAD
    documentation = "Total insurable earnings in the qualifying period"
    
    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        p = parameters(period).gov.cra.benefits.employment_insurance
        
        # Cap at maximum insurable earnings
        return min_(employment_income, p.maximum_insurable_earnings)