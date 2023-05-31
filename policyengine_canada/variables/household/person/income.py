from policyengine_canada.model_api import *


class income(Variable):
    value_type = float
    entity = Person
    label = "Personal income"
    unit = CAD
    definition_period = YEAR
