from policyengine_canada.model_api import *


class is_living_at_home(Variable):
    value_type = bool
    entity = Person
    label = "Person is living at home"
    definition_period = YEAR
