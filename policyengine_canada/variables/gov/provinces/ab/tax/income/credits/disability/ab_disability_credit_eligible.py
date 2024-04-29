from policyengine_canada.model_api import *


class ab_disability_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the Alberta disability tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period):
        return person("is_disabled", period)
