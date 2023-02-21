from policyengine_canada.model_api import *


class ProvinceName(Enum):
    AB = "Alberta"
    BC = "British Columbia"
    MB = "Manitoba"
    NB = "New Brunswick"
    NL = "Newfoundland and Labrador"
    NS = "Nova Scotia"
    NT = "Northwest Territories"
    NU = "Nunavut"
    ONT = "Ontario"
    PE = "Prince Edward Island"
    QC = "Quebec"
    SK = "Saskatchewan"
    YT = "Yukon"


class province_name(Variable):
    value_type = Enum
    possible_values = ProvinceName
    default_value = ProvinceName.ONT
    entity = Household
    label = "Province"
    definition_period = YEAR
