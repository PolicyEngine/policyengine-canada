from policyengine_canada.model_api import *


class own_children_under_19(Variable):
    value_type = int
    entity = Person
    label = "Count of one's own children younger than 19 in the household"
    definition_period = YEAR
