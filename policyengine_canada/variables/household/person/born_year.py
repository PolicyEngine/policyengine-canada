from policyengine_canada.model_api import *


class born_year(Variable):
    value_type = int
    entity = Person
    label = "Born year"
    documentation = "The year of the person was born"
    definition_period = YEAR
