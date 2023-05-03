from policyengine_canada.model_api import *


class fulltime_postsecondary_student(Variable):
    value_type = bool
    entity = Household
    label = "Is household a full-time post-secondary student"
    definition_period = YEAR
    defined_for = ProvinceCode.SK