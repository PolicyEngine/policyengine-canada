from policyengine_canada.model_api import *


class household_assets(Variable):
    value_type = float
    entity = Household
    label = "household_assets"
    documentation = "Total liquid household assets, including cash on hand, bank accounts, stocks, bonds, non-locked-in retirement savings plans, and other securities."
    unit = CAD
    definition_period = YEAR
