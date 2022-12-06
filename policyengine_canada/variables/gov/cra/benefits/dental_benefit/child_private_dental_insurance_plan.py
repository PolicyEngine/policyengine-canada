from policyengine_canada.model_api import *


class child_private_dental_insurance_plan(Variable):
    value_type = bool
    entity = Person
    label = "Child has a private insurance plan"
    definition_period = YEAR
