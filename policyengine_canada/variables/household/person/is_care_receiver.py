from policyengine_canada.model_api import *

class is_care_receiver(Variable):
    value_type = bool
    entity = Person
    label = "Is the receiver"
    definition_period = YEAR 