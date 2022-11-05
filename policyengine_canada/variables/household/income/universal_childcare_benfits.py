from policyengine_canada.model_api import *


class universal_childcare_benefits(Variable):
    value_type = float
    entity = Person
    label = "Universal childcare benefits"
    unit = CAD
    documentation = "Universal childcare benefits"
    definition_period = YEAR
