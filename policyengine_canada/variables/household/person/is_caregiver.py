from policyengine_canada.model_api import *


class is_caregiver(Variable):
    value_type = bool
    entity = Person
    label = "Is a caregiver to dependent in a household"
    definition_period = YEAR
