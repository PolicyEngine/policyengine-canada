from policyengine_canada.model_api import *


class child(Variable):
    value_type = int
    entity = Person
    label = "Children"
    unit = CAD
    documentation = "Number of dependent children under the age of 19"
    definition_period = YEAR
