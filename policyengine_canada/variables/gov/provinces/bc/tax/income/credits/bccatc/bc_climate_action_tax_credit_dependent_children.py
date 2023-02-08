from policyengine_canada.model_api import *


class bc_climate_action_tax_credit_dependent_children(Variable):
    value_type = int
    entity = Household
    label = "British Columbia Climate action tax credit dependent Children"
    unit = CAD
    documentation = "Number of eligible dependent children"
    definition_period = YEAR

    adds = ["is_child_for_bc_climate_action_tax_credit"]
