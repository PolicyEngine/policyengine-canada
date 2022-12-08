from policyengine_canada.model_api import *


class is_rural(Variable):
    value_type = bool
    entity = Household
    definition_period = ETERNITY
    label = "Is in a rural area"
    reference = ""
