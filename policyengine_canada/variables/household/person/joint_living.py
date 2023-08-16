from policyengine_canada.model_api import *


class joint_living(Variable):
    value_type = bool
    entity = Household
    label = "Cohabitating spouses"
    definition_period = YEAR
