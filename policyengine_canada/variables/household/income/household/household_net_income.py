from policyengine_canada.model_api import *


class household_net_income(Variable):
    value_type = float
    entity = Household
    label = "net income"
    unit = CAD
    definition_period = YEAR
    adds = [
        "individual_net_income",
    ]


# TODO: find better name for household net income
