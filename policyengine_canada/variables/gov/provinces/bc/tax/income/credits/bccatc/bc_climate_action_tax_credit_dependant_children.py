from policyengine_canada.model_api import *


class bc_climate_action_tax_credit_dependant_children(Variable):
    value_type = int
    entity = Household
    label = "British Columbia Climate action tax credit dependant Children"
    unit = CAD
    documentation = "Number of eligible dependant children"
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    adds = ["is_child_for_bc_climate_action_tax_credit"]
