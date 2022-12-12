from policyengine_canada.model_api import *


class dental_expenses(Variable):
    value_type = float
    entity = Person
    label = "Costs for dental care"
    unit = CAD
    definition_period = YEAR
