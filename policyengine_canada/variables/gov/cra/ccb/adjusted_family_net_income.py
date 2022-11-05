from policyengine_canada.model_api import *


class adjusted_family_net_income(Variable):
    value_type = float
    entity = Person
    label = "Adjusted family net income"
    unit = CAD
    documentation = "The family net income minus any universal child care benefit and registered disability savings plan income received"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = ["family_net_income"] - [
            "universal_childcare_benfits",
            ["registered_disability_savings_plan_income"],
        ]
