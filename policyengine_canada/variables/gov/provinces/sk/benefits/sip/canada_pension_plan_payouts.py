from policyengine_canada.model_api import *


class canada_pension_plan_payout(Variable):
    value_type = bool
    entity = Person
    label = "Canada Pension Plan yearly payout"
    definition_period = YEAR