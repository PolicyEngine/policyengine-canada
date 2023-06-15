from policyengine_canada.model_api import *


class is_caregiver(Variable):
    value_type = bool
    entity = Person
    label = "Is the care receiver"
    definition_period = YEAR
