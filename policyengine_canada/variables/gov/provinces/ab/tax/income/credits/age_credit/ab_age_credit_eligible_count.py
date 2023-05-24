from policyengine_canada.model_api import *


class ab_age_credit_eligible_count(Variable):
    value_type = int
    entity = Person
    label = "Alberta age credit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    adds = ["ab_age_credit_eligibility"]
