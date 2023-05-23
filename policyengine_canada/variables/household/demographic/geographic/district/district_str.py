from policyengine_canada.model_api import *


class district_str(Variable):
    value_type = str
    entity = Household
    label = "Dsitrict (string)"
    documentation = "District variable, stored as a string"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return household("district", period).decode_to_str()
