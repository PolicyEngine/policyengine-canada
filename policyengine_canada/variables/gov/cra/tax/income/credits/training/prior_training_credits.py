from policyengine_canada.model_api import *


class prior_training_credits(Variable):
    value_type = float
    entity = Person
    label = "Prior training credits"
    unit = CAD
    definition_period = YEAR
