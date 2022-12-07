from policyengine_canada.model_api import *


class full_custody(Variable):
    value_type = bool
    entity = Household
    label = "Has full custody of child"
    definition_period = YEAR
