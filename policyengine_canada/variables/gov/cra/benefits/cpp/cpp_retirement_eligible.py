from policyengine_canada.model_api import *


class cpp_retirement_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for CPP retirement pension"
    definition_period = YEAR
    documentation = "Whether person is eligible for CPP retirement pension"
    
    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.cpp.retirement
        
        # Check age requirement (60+)
        age = person("age", period)
        meets_age = age >= p.eligibility_age
        
        # Check contribution requirement (simplified - at least 1 year)
        years_contributed = person("cpp_years_of_contribution", period)
        has_contributions = years_contributed > 0
        
        return meets_age & has_contributions