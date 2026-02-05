from policyengine_canada.model_api import *


class special_care_home(Variable):
    value_type = bool
    entity = Person
    label = "Person is living in Special Care Home"
    definition_period = YEAR