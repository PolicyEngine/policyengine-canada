from policyengine_canada.model_api import *


class is_head_or_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Is spouse or head in a household"
    definition_period = YEAR
