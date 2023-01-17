from policyengine_canada.model_api import *


class full_time_childcare(Variable):
    value_type = bool
    entity = Household
    label = "Full-time childcare"
    unit = CAD
    definition_period = YEAR


# TODO: computation based variable - based on full-time definition
