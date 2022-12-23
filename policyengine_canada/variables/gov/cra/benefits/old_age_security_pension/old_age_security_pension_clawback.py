from policyengine_canada.model_api import *


class old_age_security_pension_clawback(Variable):
    value_type = float
    entity = Person
    label = "Old age security pension clawback"
    unit = CAD
    definition_period = YEAR
