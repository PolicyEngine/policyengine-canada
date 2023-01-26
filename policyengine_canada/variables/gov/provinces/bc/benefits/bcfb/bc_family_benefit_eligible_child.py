from policyengine_canada.model_api import *


class bc_family_benefit_eligible_child(Variable):
    value_type = float
    entity = Person
    label = "British Columbia family benefit eligible child"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(
                period
            ).gov.cra.provinces.bc.benefits.bcfb.child_eligible_age
        )
