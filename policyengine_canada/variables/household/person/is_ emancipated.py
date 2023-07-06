from policyengine_canada.model_api import *


class is_emancipated(Variable):
    value_type = bool
    entity = Person
    label = "Is emancipated by a competent authority"
    definition_period = YEAR
