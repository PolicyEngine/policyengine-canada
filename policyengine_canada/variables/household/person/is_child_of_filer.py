from policyengine_canada.model_api import *


class is_child_of_filer(Variable):
    value_type = bool
    entity = Person
    label = "Is the child of the tax filer or their spouse"
    definition_period = YEAR
