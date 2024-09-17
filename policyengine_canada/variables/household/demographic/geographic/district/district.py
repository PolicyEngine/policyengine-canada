from policyengine_canada.model_api import *
from policyengine_canada.variables.household.demographic.geographic.district.district_enum import (
    District,
)

import numpy as np


class county(Variable):
    value_type = Enum
    possible_values = District
    default_value = District.UNKNOWN
    entity = Household
    label = "District"
    definition_period = ETERNITY
