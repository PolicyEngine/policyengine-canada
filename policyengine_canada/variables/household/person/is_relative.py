from policyengine_canada.model_api import *


class is_relative(Variable):
    value_type = bool
    entity = Person
    label = "Is a relative of the household"
    definition_period = YEAR
