from policyengine_canada.model_api import *

class nb_pension_benefit(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick pension benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NB
     
    def formula(person, period, parameters):
        age = person("age", period)
        pension_income = person("pension_and_savings_plan_income", period)
        threshold = parameters(period).gov.provinces.nb.benefits.pension_benefit.age_eligibility
        maximum_benefit = parameters(period).gov.cra.provinces.nb.benefits.pension_benefit.maximum_benefit
        age_eligibility = age > threshold
        #min of 1_000 or less    
        return age_eligibility * min_(maximum_benefit, pension_income)
    