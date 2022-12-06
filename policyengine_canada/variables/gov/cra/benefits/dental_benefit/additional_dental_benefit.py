from policyengine_canada.model_api import *


class additional_dental_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada additional dental benefit"
    unit = CAD
    definition_period = YEAR
    documentation = "If dental costs exceeed $650, a household may apply for an additional payment."
