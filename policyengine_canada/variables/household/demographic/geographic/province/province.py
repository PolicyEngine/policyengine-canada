from policyengine_canada.model_api import *
from policyengine_canada.variables.household.demographic.geographic.province.province_enum import (
    Province,
)


class province(Variable):
    value_type = Enum
    possible_values = Province
    default_value = Province.UNKNOWN
    entity = Household
    label = "Province"
    definition_period = ETERNITY
