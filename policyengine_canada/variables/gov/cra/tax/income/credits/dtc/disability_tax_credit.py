from policyengine_canada.model_api import *


class disability_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Disability tax credit"
    unit = CAD
    definition_period = YEAR
    adds = ["dtc_base", "dtc_child_supplement"]
