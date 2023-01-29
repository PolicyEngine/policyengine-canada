from policyengine_canada.model_api import *


class Province(Enum):
    UNKNOWN = "Unknown"
    ALBERTA = "Alberta"
    BRITISH_COLUMBIA = "British Columbia"
    MANITOBA = "Manitoba"
    NEW_BRUNSWICK = "New Brunswick"
    NEWFOUNDLAND_AND_LABRADOR = "Newfoundland and Labrador"
    NOVA_SCOTIA = "Nova Scotia"
    NORTHWEST_TERRITORIES = "Northwest Territories"
    NUNAVUT = "Nunavut"
    ONTARIO = "Ontario"
    PRINCE_EDWARD_ISLAND = "Prince Edward Island"
    QUEBEC = "Quebec"
    SASKATCHEWAN = "Saskatchewan"
    YUKON = "Yukon"


class province(Variable):
    value_type = Enum
    possible_values = Province
    default_value = Province.UNKNOWN
    entity = Household
    label = "Province"
    definition_period = YEAR
