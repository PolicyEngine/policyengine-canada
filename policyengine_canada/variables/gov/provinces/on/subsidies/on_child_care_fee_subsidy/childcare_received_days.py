from policyengine_canada.model_api import *


class childcare_received_days(Variable):
    value_type = int
    entity = Household
    label = "Received days of childcare in a year"
    unit = CAD
    definition_period = YEAR
