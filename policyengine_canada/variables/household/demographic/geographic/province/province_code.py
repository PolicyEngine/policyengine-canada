from policyengine_core.model_api import *
from policyengine_canada.entities import *
from policyengine_canada.tools.general import *


class ProvinceCode(Enum):
    AB = "AB"
    BC = "BC"
    MB = "MB"
    NB = "NB"
    NL = "NL"
    NS = "NS"
    NT = "NT"
    NU = "NU"
    ONT = "ONT"
    PE = "PE"
    QC = "QC"
    SK = "SK"
    YT = "YT"


class province_code(Variable):
    value_type = Enum
    possible_values = ProvinceCode
    default_value = ProvinceCode.ONT
    entity = Household
    label = "Province code"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return ProvinceCode.encode(
            household("province_name", period).decode_to_str()
        )
