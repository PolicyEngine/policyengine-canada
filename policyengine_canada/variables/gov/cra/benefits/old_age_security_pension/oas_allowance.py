from policyengine_canada.model_api import *


class oas_allowance(Variable):
    value_type = float
    entity = Person
    label = "OAS Allowance for the Spouse"
    definition_period = YEAR
    unit = CAD
    documentation = "Allowance for low-income spouses of OAS pensioners aged 60-64"
    
    def formula(person, period, parameters):
        # Eligibility criteria
        age = person("age", period)
        eligible_age = (age >= 60) & (age < 65)
        
        # Check if married and spouse receives OAS
        household = person.household
        is_married = household("is_married", period)
        
        # Check if other household members receive OAS (simplified check)
        # In reality, would need to specifically check the spouse
        # Use oas_pre_repayment to avoid circular dependency with oas_net
        oas_amounts = person("oas_pre_repayment", period)
        household_oas = household.sum(oas_amounts)
        own_oas = person("oas_pre_repayment", period)
        other_members_oas = household_oas - own_oas
        spouse_receives_oas = is_married & (other_members_oas > 0)
        
        # Income test (simplified - would need combined income test)
        # This would be more complex in reality
        eligible = eligible_age & spouse_receives_oas
        
        p = parameters(period).gov.cra.benefits.old_age_security_pension
        
        # Simplified - return maximum for eligible individuals
        # In reality, this would be income-tested
        # Check if the allowance parameter exists (added in 2024)
        if hasattr(p, 'allowance') and hasattr(p.allowance, 'maximum'):
            annual_amount = p.allowance.maximum * 12
            return where(eligible, annual_amount, 0)
        else:
            # Parameter not available for this period
            return np.zeros_like(eligible)