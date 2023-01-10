from policyengine_canada.model_api import *


class child_benefit_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Children eligible for Canada Child Benefit"
    definition_period = YEAR

    adds = ["child_benefit_eligible"]
