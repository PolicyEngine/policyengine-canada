from policyengine_canada.model_api import *


class ab_disability_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Disability tax credit"
    unit = CAD
    definition_period = YEAR
    adds = ["ab_disability_base"]