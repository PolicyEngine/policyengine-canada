from policyengine_canada.model_api import *


class cpp_years_of_contribution(Variable):
    value_type = float
    entity = Person
    label = "Years of CPP contributions"
    definition_period = YEAR
    unit = "year"
    documentation = "Number of years person has contributed to CPP"