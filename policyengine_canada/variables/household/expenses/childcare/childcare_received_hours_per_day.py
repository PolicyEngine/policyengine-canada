from policyengine_canada.model_api import *


class childcare_received_hours_per_day(Variable):
    value_type = int
    entity = Household
    label = "Child care hours per day"
    unit = "hour"
    definition_period = YEAR
