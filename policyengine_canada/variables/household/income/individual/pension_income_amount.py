from policyengine_canada.model_api import *

class nb_pension_benefit(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick pension benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NB
     