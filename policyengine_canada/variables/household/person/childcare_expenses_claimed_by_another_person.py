from policyengine_canada.model_api import *


class childcare_expenses_claimed_by_another_person(Variable):
    value_type = float
    entity = Person
    label = "Amount of Childcare received which was claimed by another person"
    unit = CAD
    definition_period = YEAR
