from policyengine_canada.model_api import *


class care_expenses(Variable):
    value_type = float
    entity = Person
    label = "Amount of childcare expenses incurred by the child"
    unit = CAD
    definition_period = YEAR
