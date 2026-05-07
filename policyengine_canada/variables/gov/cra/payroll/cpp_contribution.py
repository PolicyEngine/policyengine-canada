from policyengine_canada.model_api import *


class cpp_contribution(Variable):
    value_type = float
    entity = Person
    label = "Canada Pension Plan contribution"
    definition_period = YEAR
    unit = CAD
    documentation = "Annual Canada Pension Plan contribution (first tier)"

    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        p = parameters(period).gov.cra.payroll.cpp
        
        # Total earnings
        total_earnings = employment_income + self_employment_income
        
        # Apply basic exemption and maximum to total earnings
        total_pensionable = max_(0, min_(total_earnings, p.maximum_pensionable_earnings) - p.basic_exemption)
        
        # The basic exemption is applied first to employment income, then to self-employment
        # This matches how it's done in practice for mixed income earners
        employment_after_exemption = max_(0, employment_income - p.basic_exemption)
        remaining_exemption = max_(0, p.basic_exemption - employment_income)
        self_employment_after_exemption = max_(0, self_employment_income - remaining_exemption)
        
        # Cap at maximum pensionable earnings
        employment_pensionable = min_(employment_after_exemption, p.maximum_pensionable_earnings - p.basic_exemption)
        remaining_room = max_(0, p.maximum_pensionable_earnings - p.basic_exemption - employment_pensionable)
        self_employment_pensionable = min_(self_employment_after_exemption, remaining_room)
        
        # Employment income: employee rate only
        employee_contribution = employment_pensionable * p.rate
        
        # Self-employment income: double rate (employee + employer)
        self_employed_contribution = self_employment_pensionable * p.rate * 2
        
        return employee_contribution + self_employed_contribution