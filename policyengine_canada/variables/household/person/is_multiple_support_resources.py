from policyengine_canada.model_api import *


class is_multiple_support_resources(Variable):
    value_type = bool
    entity = Person
    label = "Support Resources"
    unit = CAD
    documentation = "whether receive support from another Government of Saskatchewan income assistance or training program"
    definition_period = YEAR
