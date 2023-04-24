from policyengine_canada.model_api import *


class is_of_school_age(Variable):
    value_type = bool
    entity = Person
    label = "Child that is eligible to go to school"
    definition_period = YEAR

#TODO: find what the legal definition is of "school age"

