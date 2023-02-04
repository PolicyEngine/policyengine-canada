from policyengine_canada.model_api import *


class child_benefit(Variable):
    value_type = float
    entity = Household
    label = "Canada Child Benefit"
    unit = CAD
    documentation = (
        "Non taxable amount paid monthly per children under 18 years of age. "
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        base = household("child_benefit_base", period)
        reduction = household("child_benefit_reduction", period)
        return max_(0, base - reduction)
