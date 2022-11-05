from policyengine_canada.model_api import *


class family_net_income(Variable):
    value_type = float
    entity = Person
    label = "Family net income"
    unit = CAD
    documentation = "The family net income"
    definition_period = YEAR
