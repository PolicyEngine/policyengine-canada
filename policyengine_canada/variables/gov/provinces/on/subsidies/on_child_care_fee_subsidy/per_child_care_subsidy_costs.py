from policyengine_canada.model_api import *


class on_per_child_care_subsidy_costs(Variable):
    value_type = float
    entity = Household
    label = "Ontario per child care subsidy costs"
    unit = CAD
    definition_period = YEAR
