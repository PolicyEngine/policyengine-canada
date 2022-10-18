from policyengine_canada.model_api import *


class employment_income(Variable):
    value_type = float
    entity = Person
    label = "Employment income"
    unit = CAD
    documentation = "Income from gainful employment"
    definition_period = YEAR
