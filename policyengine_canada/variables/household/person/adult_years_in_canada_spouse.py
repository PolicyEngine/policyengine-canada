from policyengine_canada.model_api import *


class adult_years_in_canada_spouse(Variable):
    value_type = int
    entity = Household
    label = "Spouse's Adult Years In Canada"
    unit = CAD
    documentation = "Spouse's years spent in Canada since the age of 18"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        adult_years_in_canada = person("adult_years_in_canada", period)
        spouse = person("is_spouse", period)
        return household.max(adult_years_in_canada * spouse)
