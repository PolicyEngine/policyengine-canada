from policyengine_canada.model_api import *


class child_physical_activities_fees(Variable):
    value_type = float
    entity = Household
    label = "Fees for childrens physical activities"
    definition_period = YEAR
