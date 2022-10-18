from policyengine_canada.model_api import *


class household_id(Variable):
    value_type = float
    entity = Household
    label = "Household ID"
    unit = CAD
    definition_period = ETERNITY
