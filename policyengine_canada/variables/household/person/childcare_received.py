from policyengine_canada.model_api import *


class childcare_received(Variable):
    value_type = float
    entity = Person
    label = "Childcare received"
    unit = CAD
    definition_period = YEAR
