from policyengine_canada.model_api import *


class shared_custody(Variable):
    value_type = bool
    entity = Household
    label = "Has shared custody of child"
    definition_period = YEAR
