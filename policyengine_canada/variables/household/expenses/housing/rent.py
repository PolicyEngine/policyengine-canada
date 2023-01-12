from policyengine_canada.model_api import *


class rent(Variable):
    value_type = float
    entity = Person
    label = "Rent"
    unit = CAD
    definition_period = YEAR
