from policyengine_canada.model_api import *


class yt_basic_personal_amount_base(Variable):
    value_type = float
    entity = Person
    label = "Yukon basic personal amount base"
    definition_period = YEAR
    defined_for = ProvinceCode.YT
    adds = (
        "gov.provinces.yt.tax.income.credits.basic_personal_amount.base_amount"
    )
