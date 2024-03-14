from policyengine_canada.model_api import *


class household_benefits(Variable):
    value_type = float
    entity = Household
    label = "benefits"
    unit = CAD
    definition_period = YEAR
    adds = [
        "child_benefit",
        "dental_benfit",
        # Manitoba
        "mb_child_benefit",
        # New Brunswick
        "nb_child_benefit",
        # Nunavut
        "nu_child_benefit",
        # Yukon
        "yt_child_benefit",
    ]
