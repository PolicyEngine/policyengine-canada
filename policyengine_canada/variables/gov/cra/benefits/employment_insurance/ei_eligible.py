from policyengine_canada.model_api import *


class ei_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Employment Insurance"
    definition_period = YEAR
    documentation = "Whether person is eligible for Employment Insurance benefits"
    
    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.employment_insurance
        
        # Check minimum hours requirement
        insurable_hours = person("ei_insurable_hours", period)
        meets_hours = insurable_hours >= p.minimum_hours
        
        # Must have insurable earnings
        insurable_earnings = person("ei_insurable_earnings", period)
        has_earnings = insurable_earnings > 0
        
        return meets_hours & has_earnings