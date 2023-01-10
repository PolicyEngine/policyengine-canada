from policyengine_canada.model_api import *


class family_working_income(Variable):
    value_type = float
    entity = Household
    label = "Family working income"
    unit = CAD
    documentation = "Income from employment and self-employment of a family"
    definition_period = YEAR
    # A.2.(122.7)(1.1)
    reference = (
        "https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-96.html#h-299725"
    )

    adds = ["working_income"]
