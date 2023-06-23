from policyengine_canada.model_api import *


class has_spouse(Variable):
    value_type = bool
    entity = Person
    label = "The household has spouse"
    definition_period = YEAR
