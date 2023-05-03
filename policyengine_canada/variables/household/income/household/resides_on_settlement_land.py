from policyengine_canada.model_api import *


class resides_on_settlement_land(Variable):
    value_type = bool
    entity = Person
    label = "Resides on Settlement land"
    definition_period = YEAR
