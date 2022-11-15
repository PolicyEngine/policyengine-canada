from policyengine_canada.model_api import *
from policyengine_canada.variables.household.demographic.geographic.province.province_enum import (
    Province,
)
import numpy as np


class province(Variable):
    value_type = Enum
    possible_values = Province
    default_value = Province.UNKNOWN
    entity = Household
    label = "Province"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        # Attempt to look up from ZIP code
        zip_code = household("zip_code", period).astype(int)
        zip_codes = ZIP_CODE_DATASET.set_index("zip_code")
        province_name = zip_codes.province[zip_code]
        state_code = zip_codes.state[zip_code]
        province_key = province_name.apply(
            lambda name: name.replace(" ", "_")
            .replace("-", "_")
            .replace(".", "")
            .replace("'", "_")
            .strip()
            .upper()
        )
        province_state = province_key.str.cat(state_code, sep="_")
        province_names = pd.Series(
            np.arange(len(Province._member_names_)),
            index=Province._member_names_,
        )
        return province_names[province_state]
