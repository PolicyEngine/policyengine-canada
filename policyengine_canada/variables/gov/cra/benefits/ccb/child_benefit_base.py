from policyengine_canada.model_api import *


class child_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "Canada Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Canada Child Benefit before reduction."
    definition_period = YEAR

    adds = ["child_benefit_base_person"]
