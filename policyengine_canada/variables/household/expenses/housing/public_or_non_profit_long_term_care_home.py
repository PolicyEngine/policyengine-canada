from policyengine_canada.model_api import *


class public_or_non_profit_long_term_care_home_expense(Variable):
    value_type = float
    entity = Household
    label = "Amounts paid for a public or non-profit long term care home"
    unit = CAD
    definition_period = YEAR
