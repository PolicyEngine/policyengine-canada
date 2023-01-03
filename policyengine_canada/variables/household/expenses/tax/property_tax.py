from policyengine_canada.model_api import *


class property_taxes(Variable):
    value_type = float
    entity = Person
    label = "Property taxes"
    unit = CAD
    definition_period = YEAR
