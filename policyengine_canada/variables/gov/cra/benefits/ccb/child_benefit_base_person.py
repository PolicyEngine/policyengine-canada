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
        p = parameters(period).gov.cra.benefits.ccb
        full_custody = person("full_custody", period)
        return where(
            full_custody, p.base.calc(age), p.base.calc(age) / p.divisor
        )
