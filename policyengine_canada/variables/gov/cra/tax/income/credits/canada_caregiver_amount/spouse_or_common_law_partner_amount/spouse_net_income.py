from policyengine_canada.model_api import *


class spouse_net_income(Variable):
    value_type = float
    entity = Person
    label = "Spouse Net Income"
    unit = CAD
    documentation = "The net income of the spouse of the filer"
    definition_period = YEAR
