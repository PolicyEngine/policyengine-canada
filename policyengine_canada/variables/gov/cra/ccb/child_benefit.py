from policyengine_canada.model_api import *


class child_benefit(Variable):
    value_type = float
    entity = Person
    label = "Canada Child Benefit "
    unit = CAD
    documentation = (
        "Non taxable amount paid monthly per children under 18 years of age. "
    )
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("child".count, period)
        gov = parameters(period).gov.cra.ccb
        base_amount = gov.base
        reduction = gov.reduction
