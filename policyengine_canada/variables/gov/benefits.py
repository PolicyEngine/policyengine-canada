from policyengine_canada.model_api import *


class benefits(Variable):
    value_type = float
    entity = Household
    label = "benefits"
    unit = CAD
    definition_period = YEAR
    adds = [
        "child_benefit",
        "child_disability_benefit",
        "canada_workers_benefit",
        "dental_benefit",
        "oas_net",
        # Ontario programs.
        "on_benefits",
        # British Columbia programs.
        "bc_benefits",
    ]
