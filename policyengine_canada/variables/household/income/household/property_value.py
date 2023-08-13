from policyengine_canada.model_api import *


class property_value(Variable):
    value_type = float
    entity = Household
    label = "Property value"
    documentation = "Total equity in any real or personal property."
    unit = CAD
    definition_period = YEAR
