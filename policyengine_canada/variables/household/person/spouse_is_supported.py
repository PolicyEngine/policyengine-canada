from policyengine_canada.model_api import *


class spouse_is_supported(Variable):
    value_type = bool
    entity = Household
    label = "A spouse that is supported by the tax filer"
    definition_period = YEAR
