from policyengine_canada.model_api import *


class has_spouse_or_dependant(Variable):
    value_type = bool
    entity = Person
    label = "Person has a spouse or a dependant"
    definition_period = YEAR
