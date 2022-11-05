from policyengine_canada.model_api import *


class maternity_and_parental_benefit(Variable):
    value_type = float
    entity = Person
    label = "Maternity and Parental benefit"
    unit = CAD
    documentation = "Income from maternity and parental benefits"
    definition_period = YEAR
