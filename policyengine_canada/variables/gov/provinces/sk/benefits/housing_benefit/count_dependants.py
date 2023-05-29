from policyengine_canada.model_api import *


class count_dependants(Variable):
    value_type = int
    entity = Household
    label = "Number of dependants in a household"
    unit = CAD
    documentation = "Number of dependants"
    definition_period = YEAR
