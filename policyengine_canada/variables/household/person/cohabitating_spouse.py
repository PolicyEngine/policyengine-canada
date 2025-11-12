from policyengine_canada.model_api import *


class cohabitating_spouse(Variable):
    value_type = bool
    entity = Household
    label = "Lived together with the tax filer"
    definition_period = YEAR
