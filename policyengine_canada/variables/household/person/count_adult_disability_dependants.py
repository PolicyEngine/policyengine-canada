from policyengine_canada.model_api import *


class count_adult_disability_dependants(Variable):
    value_type = int
    entity = Household
    label = "disability dependants"
    unit = CAD
    documentation = "Number of adult disability dependants"
    definition_period = YEAR
    adds = ["is_disabled_dependant"]