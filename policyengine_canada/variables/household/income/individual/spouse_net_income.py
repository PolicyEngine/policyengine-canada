from policyengine_canada.model_api import *


class spouse_net_income(Variable):
    value_type = int
    entity = Household
    label = "Spouse's Individual Net Income"
    unit = CAD
    documentation = "Spouse's Individual Net Income"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        individual_net_income = person("individual_net_income", period)
        spouse = person("is_spouse", period)
        return household.max(individual_net_income * spouse)
