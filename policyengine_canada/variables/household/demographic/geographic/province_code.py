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
    ON = "ON"
    QC = "QC"
    SK = "SK"
    YT = "YT"


class state_code(Variable):
    value_type = Enum
    possible_values = ProvinceCode
    default_value = ProvinceCode.CA
    entity = Household
    label = "Province code"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        return ProvinceCode.encode(
            household("province_name", period).decode_to_str()
        )
