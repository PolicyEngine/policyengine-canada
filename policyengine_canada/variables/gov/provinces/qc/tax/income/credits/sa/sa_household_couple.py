from policyengine_canada.model_api import *


class sa_household_couple(Variable):
    value_type = int
    entity = Household
    label = "Quebec senior assistance tax credits eligible senior couple"
    definition_period = YEAR

    adds = ["sa_couple_eligibility"]
