from policyengine_canada.model_api import *


class is_full_time_student(Variable):
    value_type = bool
    entity = Person
    label = "Is the person a full-time post-secondary student"
    definition_period = YEAR
    defined_for = ProvinceCode.SK
