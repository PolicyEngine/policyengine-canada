from policyengine_canada.model_api import *


class is_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Is household spouse"
    definition_period = YEAR
