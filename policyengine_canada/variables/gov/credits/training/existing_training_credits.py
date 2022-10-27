from policyengine_canada.model_api import *


class existing_training_credits(Variable):
    value_type = float
    entity = Person
    label = "Existing training credits"
    unit = CAD
    documentation = "Previously existing training credits"
    definition_period = YEAR


# Threshold: $5,000 total
