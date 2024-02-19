from policyengine_canada.model_api import *


class care_expenses(Variable):
    value_type = float
    entity = Person
    label = "Amount of care expenses incurred by the person"
    unit = CAD
    definition_period = YEAR
