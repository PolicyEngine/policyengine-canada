from policyengine_canada.model_api import *


class household_net_income(Variable):
    value_type = float
    entity = Household
    label = "net income"
    unit = CAD
    definition_period = YEAR
    adds = [
        "individual_net_income",
        "household_benefits",
    ]


class household_net_income(Variable):
    value_type = float
    entity = Household
    label = "benfits"
    unit = CAD
    definition_period = YEAR
    adds = [
        "ccb",
        "cdb",
        "cwb",
        "dental_benefit",
        "old_age_security_pension",
    ]


# TODO: find better name for household net income
