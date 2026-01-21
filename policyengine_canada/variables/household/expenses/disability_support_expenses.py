from policyengine_canada.model_api import *


class disability_support_expenses(Variable):
    value_type = float
    entity = Person
    label = "Disability Support Expenses"
    definition_period = YEAR
