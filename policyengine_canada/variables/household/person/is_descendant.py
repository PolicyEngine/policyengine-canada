from policyengine_canada.model_api import *


class is_decendant(Variable):
    value_type = bool
    entity = Person
    label = "Is decendant of the household"
    definition_period = YEAR
