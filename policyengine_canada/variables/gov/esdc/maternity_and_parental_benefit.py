from policyengine_canada.model_api import *


class maternity_and_parental_benefit(Variable):
    value_type = float
    entity = Person
    label = "Employment Insurance maternity and parental benefits"
    unit = CAD
    definition_period = YEAR
