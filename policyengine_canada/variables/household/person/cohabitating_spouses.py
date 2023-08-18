from policyengine_canada.model_api import *


class cohabitating_spouses(Variable):
    value_type = bool
    entity = Household
    label = "Cohabitating spouses"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        spouse = person("is_spouse", period)
        return household.any(spouse)
