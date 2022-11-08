from policyengine_canada.model_api import *


class child_benefit(Variable):
    value_type = float
    entity = Person
    label = "Canada Child Benefit "
    unit = CAD
    documentation = (
        "Non taxable amount paid monthly per children under 18 years of age. "
    )
    definition_period = YEAR
