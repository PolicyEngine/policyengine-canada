from policyengine_canada.model_api import *


class care_costs_for_self(Variable):
    value_type = float
    entity = Person
    label = "Canadian care cost for self"
    unit = CAD
    definition_period = YEAR
