from policyengine_canada.model_api import *


class is_custodied_by_filer(Variable):
    value_type = bool
    entity = Person
    label = "Is custodied or supervised by the tax filer or their spouse"
    definition_period = YEAR
