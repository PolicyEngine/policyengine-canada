from policyengine_canada.model_api import *


class childcare_received_hours(Variable):
    value_type = int
    entity = Household
    label = "Received hours of childcare"
    unit = CAD
    definition_period = YEAR
