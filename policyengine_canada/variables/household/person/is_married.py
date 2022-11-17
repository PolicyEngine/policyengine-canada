from policyengine_canada.model_api import *


class is_married(Variable):
    value_type = bool
    entity = Person
    label = "Is married"
    unit = CAD
    documentation = "Person is part of a marriage"
    definition_period = YEAR
