from policyengine_canada.model_api import *


class low_income_housing(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan Social Housing Program"
    unit = CAD
    definition_period = YEAR