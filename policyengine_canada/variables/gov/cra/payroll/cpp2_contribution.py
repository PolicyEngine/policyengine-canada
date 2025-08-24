from policyengine_canada.model_api import *


class cpp2_contribution(Variable):
    value_type = float
    entity = Person
    label = "CPP2 contribution"
    definition_period = YEAR
    unit = CAD
    documentation = "Second additional Canada Pension Plan contribution (enhanced tier)"

    def formula(person, period, parameters):
        # CPP2 only started in 2024
        if period.start.year < 2024:
            return person.empty_array()
            
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        p_cpp = parameters(period).gov.cra.payroll.cpp
        p_cpp2 = parameters(period).gov.cra.payroll.cpp2
        
        # Total earnings
        total_earnings = employment_income + self_employment_income
        
        # CPP2 applies to earnings between YMPE and YAMPE
        cpp2_earnings_floor = p_cpp.maximum_pensionable_earnings
        cpp2_earnings_ceiling = p_cpp2.additional_maximum_pensionable_earnings
        
        # Calculate pensionable earnings for CPP2 (earnings between YMPE and YAMPE)
        cpp2_pensionable = max_(0, min_(total_earnings, cpp2_earnings_ceiling) - cpp2_earnings_floor)
        
        if total_earnings == 0 or cpp2_pensionable == 0:
            return person.empty_array()
        
        # Allocate CPP2 pensionable earnings proportionally
        # First check how much of total earnings is above YMPE
        earnings_above_ympe = max_(0, total_earnings - cpp2_earnings_floor)
        
        if earnings_above_ympe == 0:
            return person.empty_array()
            
        # Allocate the CPP2 pensionable amount based on which income is above YMPE
        employment_above_ympe = max_(0, employment_income - cpp2_earnings_floor)
        self_employment_above_ympe = max_(0, earnings_above_ympe - employment_above_ympe)
        
        # Calculate actual pensionable amounts (capped at YAMPE - YMPE)
        employment_cpp2_pensionable = min_(employment_above_ympe, cpp2_pensionable)
        self_employment_cpp2_pensionable = min_(self_employment_above_ympe, cpp2_pensionable - employment_cpp2_pensionable)
        
        # Employment income: employee rate only
        employee_cpp2 = employment_cpp2_pensionable * p_cpp2.rate
        
        # Self-employment income: double rate (employee + employer)
        self_employed_cpp2 = self_employment_cpp2_pensionable * p_cpp2.rate * 2
        
        return employee_cpp2 + self_employed_cpp2