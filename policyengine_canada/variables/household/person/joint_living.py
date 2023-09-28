from policyengine_canada.model_api import *


class joint_living(Variable):
    value_type = bool
    entity = Household
    label = "Live together with the tax filer"
    unit = CAD
    definition_period = YEAR