from policyengine_canada.model_api import *


class lived_in_a_student_residence(Variable):
    value_type = bool
    entity = Household
    label = "Student residence"
    unit = CAD
    documentation = "A person who lived in a stundet residence"
    definition_period = YEAR
