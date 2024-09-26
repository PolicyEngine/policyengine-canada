from policyengine_canada.model_api import *


class household_head_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Basic Personal Amount of the household head"
    unit = CAD
    definition_period = YEAR

    adds = ["basic_personal_amount"]


# TODO: adjust variables around household level BPA
