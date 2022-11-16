from policyengine_canada.model_api import *


class is_single_parent(Variable):
    value_type = bool
    entity = Person
    label = "Is a single parent"
    unit = CAD
    documentation = "Person is a single parent"
    definition_period = YEAR
