from policyengine_canada.model_api import *


class is_related(Variable):
    value_type = bool
    entity = Person
    label = "A person related to the tax filer"
    definition_period = YEAR
