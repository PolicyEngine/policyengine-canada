from policyengine_canada.model_api import *


class is_own_child(Variable):
    value_type = bool
    entity = Person
    label = "Is his or her parents' own child"
    definition_period = YEAR
