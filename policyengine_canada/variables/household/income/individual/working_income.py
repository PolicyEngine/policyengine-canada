from policyengine_canada.model_api import *


class employment_income(Variable):
    value_type = float
    entity = Person
    label = "Working income"
    unit = CAD
    documentation = "Income from employment as well as self-employment"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("employment_income", period) + person(
            "self_employment_income", period
        )
