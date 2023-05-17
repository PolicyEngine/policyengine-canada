from policyengine_canada.model_api import *


class household_assets(Variable):
    value_type = float
    entity = Household
    unit = CAD
    label = "The value of household assets"
    definition_period = YEAR