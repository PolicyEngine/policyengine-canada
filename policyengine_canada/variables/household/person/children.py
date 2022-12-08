from policyengine_canada.model_api import *


class children(Variable):
    value_type = int
    entity = Household
    label = "Children"
    unit = CAD
    documentation = "Number of dependent children under the age of 19"
    definition_period = YEAR
