from policyengine_canada.model_api import *


class childcare_received_days(Variable):
    value_type = int
    entity = Household
    label = "Received days of child care in a year"
    unit = "day"
    definition_period = YEAR
