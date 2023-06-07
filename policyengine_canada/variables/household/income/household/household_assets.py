from policyengine_canada.model_api import *


class household_assets(Variable):
    value_type = float
    entity = Household
    label = "household_assets"
    documentation = "Total liquid household assets."
    unit = CAD
    definition_period = YEAR
