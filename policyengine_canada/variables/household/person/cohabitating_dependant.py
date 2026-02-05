from policyengine_canada.model_api import *


class cohabitating_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Dependant lives together with the tax filer"
    unit = CAD
    definition_period = YEAR
