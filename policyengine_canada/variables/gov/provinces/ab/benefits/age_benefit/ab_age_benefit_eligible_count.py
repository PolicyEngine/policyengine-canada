from policyengine_canada.model_api import *


class ab_age_benefit_eligible_count(Variable):
    value_type = int
    entity = Person
    label = "Alberta age benefit eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    adds = ["ab_age_benefit_eligibility"]
