from policyengine_canada.model_api import *


class full_custody(Variable):
    value_type = bool
    entity = Person
    label = "Is in full custody of the household head"
    definition_period = YEAR
