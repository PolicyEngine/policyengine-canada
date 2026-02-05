from policyengine_canada.model_api import *


class lived_together(Variable):
    value_type = bool
    entity = Person
    label = "Lived together with the tax filer"
    definition_period = YEAR
