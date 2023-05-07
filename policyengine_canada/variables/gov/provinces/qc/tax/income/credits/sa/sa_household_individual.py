from policyengine_canada.model_api import *


class sa_household_individual(Variable):
    value_type = int
    entity = Household
    label = "Quebec senior assistance tax credits for family with only one eligible senior"
    definition_period = YEAR

    adds = ["sa_individual_eligibility"]
