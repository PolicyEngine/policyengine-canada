from policyengine_canada.model_api import *


class receipient_age(Variable):
    value_type = int
    entity = Person
    label = "Age"
    documentation = "Receipient's Age in years since birth"
    definition_period = YEAR
    defined_for = ProvinceCode.SK