from policyengine_canada.model_api import *


class received_allowance(Variable):
    value_type = float
    entity = Person
    label = "Amount of allowance received"
    definition_period = YEAR
