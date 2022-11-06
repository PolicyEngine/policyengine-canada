from policyengine_canada.model_api import *


class universal_child_care_benefit(Variable):
    value_type = float
    entity = Person
    label = "Universal child care benefit"
    unit = CAD
    documentation = "Universal child care benefit (UCCB) ended in 2016."
    definition_period = YEAR
