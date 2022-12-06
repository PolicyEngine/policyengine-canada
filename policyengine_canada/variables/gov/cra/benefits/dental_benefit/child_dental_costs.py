from policyengine_canada.model_api import *


class child_dental_costs(Variable):
    value_type = float
    entity = Household
    label = "Costs for dental care occured for a child in canada"
    unit = CAD
    definition_period = YEAR
