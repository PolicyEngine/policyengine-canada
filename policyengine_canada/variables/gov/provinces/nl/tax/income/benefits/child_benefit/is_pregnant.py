from policyengine_canada.model_api import *


class is_pregnant(Variable):
    value_type = bool
    entity = Person
    label = "Is pregnant"
    definition_period = YEAR
