from policyengine_canada.model_api import *


class eligible_people_for_other_infirm_dependants_amount(Variable):
    value_type = int
    entity = Person
    label = "Number of eligible dependants for the Canada caregiver amount for other infirm dependants - Line 30450"
    definition_period = YEAR

    adds = ["eligible_dependent_for_other_infirm_dependants_amount"]
