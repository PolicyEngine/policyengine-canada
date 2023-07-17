from policyengine_canada.model_api import *


class sk_dependant_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan dependant eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK