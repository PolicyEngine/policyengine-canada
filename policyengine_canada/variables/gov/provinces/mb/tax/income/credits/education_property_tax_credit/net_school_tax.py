from policyengine_canada.model_api import *


class net_school_tax(Variable):
    value_type = float
    entity = Household
    label = "Net school tax paid"
    unit = CAD
    definition_period = YEAR
