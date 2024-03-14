from policyengine_canada.model_api import *


class household_benefits(Variable):
    value_type = float
    entity = Household
    label = "benefits"
    unit = CAD
    definition_period = YEAR
    adds = [
        "mb_child_benefit",
        "nb_child_benefit",
        "nu_child_benefit",
        "yt_child_benefit",
    ]
