from policyengine_canada.model_api import *


class is_carereceiver(Variable):
    value_type = bool
    entity = Person
    label = "Is a care receiver"
    definition_period = YEAR
