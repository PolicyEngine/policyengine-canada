from policyengine_canada.model_api import *

class nb_pension_benefit(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick pension benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NB
    adds = "gov.provinces.nb.benefits.benefits"
     
    def formula(person, period, parameters):
        age = person("age", period)
        pension_income = person("pension_and_savings_plan_income", period)
        threshold = parameters(period).gov.provinces.nb.benefits.pension_benefit.age_eligibility
        age_eligibility = age > threshold
    
    