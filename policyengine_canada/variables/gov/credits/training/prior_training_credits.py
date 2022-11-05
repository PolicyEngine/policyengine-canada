from policyengine_canada.model_api import *


class prior_training_credits(Variable):
    value_type = float
    entity = Person
    label = "Existing training credits"
    unit = CAD
    documentation = "Previously existing training credits"
    definition_period = YEAR
