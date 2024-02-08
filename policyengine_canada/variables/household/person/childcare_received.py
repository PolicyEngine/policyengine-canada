from policyengine_canada.model_api import *


class childcare_received(Variable):
    value_type = float
    entity = Person
    label = "Amount of Childcare received which was claimed by another person"
    unit = CAD
    definition_period = YEAR
