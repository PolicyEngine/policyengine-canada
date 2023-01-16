from policyengine_canada.model_api import *


class on_child_care_fee_subsidy(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Care Fee Subsidy"
    unit = CAD
    definition_period = YEAR
