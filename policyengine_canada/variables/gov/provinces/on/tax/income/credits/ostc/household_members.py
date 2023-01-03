from policyengine_canada.model_api import *


class household_members(Variable):
    value_type = int
    entity = Household
    label = "Members in household"
    definition_period = YEAR

    def formula(household, period, parameters):
        return household.nb_persons()
