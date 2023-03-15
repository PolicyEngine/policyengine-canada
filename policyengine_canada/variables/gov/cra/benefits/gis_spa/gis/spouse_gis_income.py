from policyengine_canada.model_api import *

class spouse_gis_income(Variable):
    value_type = int
    entity = Household
    label = "Spouse's Individual Net Income"
    unit = CAD
    documentation = "Spouse's Individual Net Income"
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        gis_income = person("gis_income", period)
        spouse = person("is_spouse", period)
        return household.max(gis_income * spouse)


