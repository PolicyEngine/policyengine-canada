from policyengine_canada.model_api import *


class yt_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon basic personal amount"
    definition_period = YEAR
    defined_for = ProvinceCode.YT
    adds = [
        "yt_basic_personal_amount_base",
        "yt_basic_personal_amount_additional",
    ]
