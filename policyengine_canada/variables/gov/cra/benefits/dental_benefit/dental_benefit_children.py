from policyengine_canada.model_api import *


class dental_benefit_children(Variable):
    value_type = int
    entity = Household
    label = "Dental benefit children"
    unit = CAD
    documentation = "Number of eligible children for the dental benefit"
    definition_period = YEAR

    formula = sum_of_variables(["is_child_for_dental_benefit"])
