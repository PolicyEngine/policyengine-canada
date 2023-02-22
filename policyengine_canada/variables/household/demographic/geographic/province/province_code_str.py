from policyengine_canada.model_api import *


class province_code_str(Variable):
    value_type = str
    entity = Household
    label = "Province code (string)"
    documentation = "Province code variable, stored as a string"
    definition_period = YEAR

    def formula(household, period, parameters):
        return household("province_code", period).decode_to_str()
