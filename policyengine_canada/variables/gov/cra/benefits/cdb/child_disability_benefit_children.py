from policyengine_canada.model_api import *


class child_disability_benefit_children(Variable):
    value_type = float
    entity = Household
    label = "Canada Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Canada Child Benefit before reduction."
    definition_period = YEAR

    formula = sum_of_variables(["child_disability_benefit_eligible_children"])
