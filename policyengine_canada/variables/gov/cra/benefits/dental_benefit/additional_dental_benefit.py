from policyengine_canada.model_api import *


class additional_dental_benefit(Variable):
    value_type = float
    entity = Household
    label = "Additional dental benefit"
    unit = CAD
    definition_period = YEAR
    documentation = "If dental costs exceed a threshold, a household may apply for an additional payment."
