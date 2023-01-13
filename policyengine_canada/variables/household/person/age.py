from policyengine_canada.model_api import *


class age(Variable):
    value_type = int
    entity = Person
    label = "Age"
    documentation = "Age in years since birth"
    definition_period = YEAR
    default_value = 18
