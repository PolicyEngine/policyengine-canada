from policyengine_canada.model_api import *


class utilities_costs(Variable):
    value_type = float
    entity = Household
    label = "Costs for utilities"
    unit = CAD
    definition_period = YEAR