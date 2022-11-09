from policyengine_canada.model_api import *


class child_benefit_base_person(Variable):
    value_type = float
    entity = Household
    label = "Canada Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Canada Child Benefit before reduction."
    definition_period = YEAR

    def formula(household, period, parameters):
        person = household.members
        age = person("age", period)
        person_amount = parameters(period).gov.cra.ccb.base.calc(age)
        return household.sum(person_amount)
