from policyengine_canada.model_api import *


class physical_activities_fees(Variable):
    value_type = float
    entity = Person
    label = "Fees for physical activities"
    definition_period = YEAR
    unit = CAD
