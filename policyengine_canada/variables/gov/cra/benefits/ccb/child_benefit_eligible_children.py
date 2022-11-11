from policyengine_canada.model_api import *


class child_benefit_eligible_children(Variable):
    value_type = float
    entity = Household
    label = "Children eligible for Canada Child Benefit"
    unit = "Person"
    documentation = "Base amount of Canada Child Benefit before reduction."
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        eligible = person("child_benefit_base_person", period) > 0
        return household.sum(eligible)
