from policyengine_canada.model_api import *


class age_spouse(Variable):
    value_type = int
    entity = Household
    label = "Spouse's Age"
    unit = CAD
    documentation = "Age of spouse in years since birth"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        age = person("age", period)
        spouse = person("is_spouse", period)
        return household.max(age * spouse)




