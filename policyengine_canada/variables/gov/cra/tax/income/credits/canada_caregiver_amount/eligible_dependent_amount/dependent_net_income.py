from policyengine_canada.model_api import *


class dependent_net_income(Variable):
    value_type = float
    entity = Person
    label = "Dependent Net Income"
    unit = CAD
    documentation = "The net income of the dependent of the filer"
    definition_period = YEAR
