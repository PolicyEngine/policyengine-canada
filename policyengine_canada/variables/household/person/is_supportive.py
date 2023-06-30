from policyengine_canada.model_api import *


class is_supportive(Variable):
    value_type = bool
    entity = Person
    label = "A person is supporting or being supported by"
    definition_period = YEAR