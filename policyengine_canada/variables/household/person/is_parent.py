from policyengine_canada.model_api import *


class is_parent(Variable):
    value_type = bool
    entity = Person
    label = "Is parent"
    definition_period = YEAR
