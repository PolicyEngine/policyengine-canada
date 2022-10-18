from policyengine_canada.model_api import *


class person_id(Variable):
    value_type = float
    entity = Person
    label = "Person ID"
    unit = CAD
    definition_period = ETERNITY
