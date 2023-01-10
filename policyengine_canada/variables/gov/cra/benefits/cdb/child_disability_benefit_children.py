from policyengine_canada.model_api import *


class child_disability_benefit_children(Variable):
    value_type = int
    entity = Household
    label = "Children eligible for the Child Disability Benefit"
    definition_period = YEAR

    adds = ["child_disability_benefit_eligible"]
