from policyengine_canada.model_api import *


class registered_disability_savings_plan_income(Variable):
    value_type = float
    entity = Person
    label = "Registered disability savings plan income"
    unit = CAD
    documentation = "Registered disability savings plan income"
    definition_period = YEAR
