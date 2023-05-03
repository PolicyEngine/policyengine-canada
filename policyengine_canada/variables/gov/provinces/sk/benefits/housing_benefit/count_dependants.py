from policyengine_canada.model_api import *


class count_dependants(Variable):
    value_type = int
    entity = Household
    label = "Dependants"
    unit = CAD
    documentation = "Number of dependants" #question: what is the definition of dependant? Does it contain the old? And if it only means child, what is the age threshold?(19 or 18?)
                                           #(If it is 19, then we could delete this variable and use the "count_children" under household )
    definition_period = YEAR