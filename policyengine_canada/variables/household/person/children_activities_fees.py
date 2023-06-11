from policyengine_canada.model_api import *


class children_activities_fees(Variable):
    value_type = float
    entity = Person
    label = "Fees for children's activities"
    definition_period = YEAR
    unit = CAD
