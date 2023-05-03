from policyengine_canada.model_api import *


class cost_on_utilities(Variable):
    value_type = float
    entity = Person
    label = "cost_on_utilities"
    unit = CAD
    definition_period = YEAR