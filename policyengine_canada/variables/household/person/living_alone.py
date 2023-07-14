from policyengine_canada.model_api import *


class living_alone(Variable):
    value_type = bool
    entity = Household
    label = "Is living alone"
    documentation = "A person who living alone"
    definition_period = YEAR
