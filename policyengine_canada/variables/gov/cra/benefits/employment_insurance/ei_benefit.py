from policyengine_canada.model_api import *


class ei_benefit(Variable):
    value_type = float
    entity = Person
    label = "Employment Insurance benefit"
    definition_period = YEAR
    unit = CAD
    documentation = "Annual Employment Insurance benefit amount"
    adds = ["ei_benefit"]
    
    def formula(person, period, parameters):
        # Get the weekly benefit amount
        weekly_benefit = person("ei_weekly_benefit", period)
        
        # For simplicity, assume 26 weeks of benefits (halfway between min 14 and max 45)
        weeks_of_benefits = 26
        
        return weekly_benefit * weeks_of_benefits