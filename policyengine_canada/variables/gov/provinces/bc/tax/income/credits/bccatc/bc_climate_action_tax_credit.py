from policyengine_canada.model_api import *


class bc_climate_action_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "British Columbia Climate Action Tax Credit after reduction"
    unit = CAD
    documentation = "Universal amount without adjustment based on AFNI"
    definition_period = YEAR

    def formula(household, period, parameters):
        