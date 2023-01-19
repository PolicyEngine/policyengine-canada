from policyengine_canada.model_api import *


class grants(Variable):
    value_type = float
    entity = Household
    label = "grants"
    unit = CAD
    definition_period = YEAR
    adds = [
        # Ontario programs.
        "on_grants",
    ]
