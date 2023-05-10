from policyengine_canada.model_api import *


class spouse_age(Variable):
    value_type = int
    entity = Person
    label = "Age"
    documentation = "Spouse's Age in years since birth"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

#dont need new varibale - use "age.py"