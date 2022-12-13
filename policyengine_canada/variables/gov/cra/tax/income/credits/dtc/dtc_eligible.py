from policyengine_canada.model_api import *


class dtc_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Is eligible for the disability tax credit"
    definition_period = YEAR
