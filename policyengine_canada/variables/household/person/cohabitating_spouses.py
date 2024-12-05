from policyengine_canada.model_api import *


class cohabitating_spouses(Variable):
    value_type = bool
    entity = Household
    label = "Cohabitating spouses"
    definition_period = YEAR
