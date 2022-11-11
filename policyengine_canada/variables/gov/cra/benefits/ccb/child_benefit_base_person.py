from policyengine_canada.model_api import *


class child_benefit_base_person(Variable):
    value_type = float
    entity = Person
    label = "Canada Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Canada Child Benefit before reduction."
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        return parameters(period).gov.cra.benefits.ccb.base.calc(age)
