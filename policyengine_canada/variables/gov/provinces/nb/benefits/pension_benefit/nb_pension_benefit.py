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
        income = person ("adjusted_personal_income", period)
        return parameters(period).gov.provinces.nb.benefits.benefits(
            income
        )