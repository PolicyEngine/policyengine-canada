from policyengine_canada.model_api import *


class is_head(Variable):
    value_type = bool
    entity = Person
    label = "Is household head"
    definition_period = YEAR
