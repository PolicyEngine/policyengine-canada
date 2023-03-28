from policyengine_canada.model_api import *


class nu_cost_of_living_credit(Variable):
    value_type = float
    entity = Person
    label = "Nunavut cost of living credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    adds = [
        "nu_cost_of_living_basic_credit",
        "nu_cost_of_living_credit_supplement",
    ]
