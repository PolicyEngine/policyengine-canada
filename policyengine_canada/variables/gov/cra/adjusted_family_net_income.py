from policyengine_canada.model_api import *


class adjusted_family_net_income(Variable):
    value_type = float
    entity = Household
    label = "Adjusted family net income"
    unit = CAD
    documentation = "The family net income minus any universal child care benefit and registered disability savings plan income received"
    definition_period = YEAR

    adds = ["family_net_income"]
    subtracts = [
        "universal_child_care_benefit",
        "registered_disability_savings_plan_income",
    ]
