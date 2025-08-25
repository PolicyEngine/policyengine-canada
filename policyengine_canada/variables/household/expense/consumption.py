from policyengine_canada.model_api import *


class consumption(Variable):
    value_type = float
    entity = Household
    label = "Household consumption"
    definition_period = YEAR
    unit = CAD
    documentation = "Total household consumption spending subject to sales tax"