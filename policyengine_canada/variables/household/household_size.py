from policyengine_canada.model_api import *


class household_size(Variable):
    value_type = int
    entity = Household
    label = "Size of a household"
    definition_period = YEAR

    def formula(household, period, parameters):
        return household.nb_persons()
