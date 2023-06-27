from policyengine_canada.model_api import *


class live_together_with_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Live with Spouse"
    unit = CAD
    documentation = (
        "A person who lives together with spouse or common-law partner"
    )
    definition_period = YEAR
