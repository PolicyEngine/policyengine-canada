from policyengine_canada.model_api import *


class is_cwb_family(Variable):
    value_type = bool
    entity = Household
    label = "Is a family for the Canada Workers Benefit"
    definition_period = YEAR

    def formula(household, period, parameters):
        # Check if there's a spouse.
        has_spouse = household("is_married", period)
        # Check if there are any dependants.
        has_dependants = add(household, period, ["cwb_dependant"]) > 0
        return has_spouse | has_dependants
