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
        
        # For now, use the maximum weekly benefit to infer max insurable earnings
        # Maximum insurable earnings = max_weekly_benefit / rate
        p = parameters(period).gov.cra.benefits.employment_insurance
        max_insurable = p.maximum_weekly_benefit / p.rate * 52
        
        # Cap at maximum insurable earnings
        return min_(employment_income, max_insurable)