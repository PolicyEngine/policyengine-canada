from policyengine_canada.model_api import *


class lived_outside_of_Whitehorse(Variable):
    value_type = bool
    entity = Household
    label = "lived outside of Whitehorse"
    unit = CAD
    documentation = "A person who lived outside of Whitehorse"
    definition_period = YEAR
