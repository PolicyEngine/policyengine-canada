from policyengine_canada.model_api import *


class adult_years_in_canada(Variable):
    value_type = int
    entity = Person
    label = "Adult Years In Canada"
    unit = CAD
    documentation = "Years spent in Canada after the age of 18"
    definition_period = YEAR
