from policyengine_canada.model_api import *


class sk_head_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan head of household eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK
