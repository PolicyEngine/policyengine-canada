from policyengine_canada.model_api import *


class canadian_armed_forces_and_personnel_deduction(Variable):
    value_type = float
    entity = Person
    label = "Canadian armed forces and personnel deduction"
    unit = CAD
    definition_period = YEAR
