from policyengine_canada.model_api import *


class cpp_retirement_pension(Variable):
    value_type = float
    entity = Person
    label = "CPP retirement pension"
    definition_period = YEAR
    unit = CAD
    documentation = "Annual CPP retirement pension amount"
    
    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.cpp.retirement
        
        # Check eligibility
        eligible = person("cpp_retirement_eligible", period)
        
        # Simplified calculation based on years of contribution
        # Use average between 0 and maximum based on contribution years
        years_contributed = person("cpp_years_of_contribution", period)
        
        # Assume full contributions after 40 years
        contribution_factor = min_(years_contributed / 40, 1)
        
        # Calculate monthly amount between 0 and maximum
        # For simplicity, use average as midpoint
        monthly_amount = contribution_factor * p.average_monthly
        
        # Convert to annual
        annual_amount = monthly_amount * 12
        
        return where(eligible, annual_amount, 0)