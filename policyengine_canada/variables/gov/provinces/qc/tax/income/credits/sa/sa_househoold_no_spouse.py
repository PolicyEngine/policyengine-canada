from policyengine_canada.model_api import *


class sa_household_no_spouse(Variable):
    value_type = int
    entity = Household
    label = "Quebec senior assistance tax credits eligible senior who did not have a spouse"
    definition_period = YEAR

    adds = ["sa_no_spouse_eligibility"]

    
