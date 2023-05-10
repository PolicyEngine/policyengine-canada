from policyengine_canada.model_api import *


class is_penioner(Variable):
    value_type = bool
    entity = Person
    label = "Is client a penioner"
    definition_period = YEAR