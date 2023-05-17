from policyengine_canada.model_api import *


class saskatchewan_income_assistance(Variable):
    value_type = bool
    entity = Household
    label = "Support Resources"
    unit = CAD
    documentation = "whether receive support from another Government of Saskatchewan income assistance or training program"
    definition_period = YEAR
