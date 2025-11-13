from policyengine_canada.model_api import *


class ei_premium(Variable):
    value_type = float
    entity = Person
    label = "Employment Insurance premium"
    definition_period = YEAR
    unit = CAD
    documentation = "Annual Employment Insurance premium paid by employee"

    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        p = parameters(period).gov.cra.payroll.ei
        
        # EI applies to employment income up to the maximum
        insurable_earnings = min_(employment_income, p.maximum_insurable_earnings)
        
        # Calculate premium
        premium = insurable_earnings * p.rate
        
        return premium