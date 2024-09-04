from policyengine_canada.model_api import *


class specialized_respite_services_expenses(Variable):
    value_type = float
    entity = Person
    label = "Expenses incurred for specialized respite services"
    unit = CAD
    definition_period = YEAR
