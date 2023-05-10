from policyengine_canada.model_api import *


class is_spouse_receiving_allowance(Variable):
    value_type = bool
    entity = Person
    label = "Is household spouse receiving allowance"
    definition_period = YEAR