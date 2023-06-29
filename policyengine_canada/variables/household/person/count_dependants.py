from policyengine_canada.model_api import *


class count_dependants(Variable):
    value_type = int
    entity = Household
    label = "Dependannts"
    unit = CAD
    documentation = "Number of dependants"
    definition_period = YEAR
    adds = ["is_dependant"]
