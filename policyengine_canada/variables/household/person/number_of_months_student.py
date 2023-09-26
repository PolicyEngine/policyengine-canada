from policyengine_canada.model_api import *


class number_of_months_student(Variable):
    value_type = float
    entity = Person
    label = "Student Months"
    unit = CAD
    documentation = "Number of months being a student"
    definition_period = YEAR
