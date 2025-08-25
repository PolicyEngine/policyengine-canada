from policyengine_canada.model_api import *


class ei_weekly_benefit(Variable):
    value_type = float
    entity = Person
    label = "Employment Insurance weekly benefit"
    definition_period = YEAR
    unit = CAD
    documentation = "Weekly Employment Insurance benefit amount (calculated annually)"
    
    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.employment_insurance
        
        # Check eligibility
        eligible = person("ei_eligible", period)
        
        # Calculate average weekly earnings
        # Simplified - using annual earnings divided by 52
        insurable_earnings = person("ei_insurable_earnings", period)
        weekly_earnings = insurable_earnings / 52
        
        # Apply benefit rate
        benefit_amount = weekly_earnings * p.rate
        
        # Cap at maximum
        capped_benefit = min_(benefit_amount, p.maximum_weekly_benefit)
        
        return where(eligible, capped_benefit, 0)