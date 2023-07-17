from policyengine_canada.model_api import *


class count_disability_claims(Variable):
    value_type = int
    entity = Household
    label = "disability claims"
    unit = CAD
    documentation = "Number of household disability claims"
    definition_period = YEAR
    adds = ["is_disabled_head_or_dependant"]