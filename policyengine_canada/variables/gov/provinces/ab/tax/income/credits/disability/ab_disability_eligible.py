from policyengine_canada.model_api import *


class ab_disability_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Is eligible for the Alberta disability tax credit"
    definition_period = YEAR
