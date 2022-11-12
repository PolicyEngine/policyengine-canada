from policyengine_canada.model_api import *


class deductions_from_total_to_net_income(Variable):
    value_type = float
    entity = Person
    label = "Deductions from Total to Net Income"
    unit = CAD
    documentation = "Deductions used in the calculation of Net Income"
    definition_period = YEAR
    reference = "SPSD/M 29.0 Variable Guide, Page 8"
