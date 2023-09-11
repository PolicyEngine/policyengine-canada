from policyengine_canada.model_api import *


class real_and_personal_property(Variable):
    value_type = float
    entity = Household
    label = "Property value"
    documentation = "Total equity in real property (land and attached assets) and personal property (tangible and intangible possessions apart from real estate)."
    unit = CAD
    definition_period = YEAR
