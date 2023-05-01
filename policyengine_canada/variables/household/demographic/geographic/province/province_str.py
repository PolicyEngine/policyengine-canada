from policyengine_canada.model_api import *


class province_str(Variable):
    value_type = str
    entity = Household
    label = "Province (string)"
    documentation = "Province variable, stored as a string"
    definition_period = YEAR

    def formula(household, period, parameters):
        return household("province", period).decode_to_str()
