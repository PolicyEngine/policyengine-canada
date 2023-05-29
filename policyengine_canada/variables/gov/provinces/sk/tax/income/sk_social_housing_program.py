from policyengine_canada.model_api import *


class sk_social_housing_program(Variable):
    value_type = bool
    entity = Person
    label = "Saskatchewan Social Housing Program"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.SK