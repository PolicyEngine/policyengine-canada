from policyengine_canada.model_api import *


class ontario_child_benefit_base(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Benefit Base"
    unit = CAD
    documentation = "Base amount of Ontario Child Benefit before reduction."
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        return parameters(period).gov.provinces.on.benefits.ocb.base.calc(
            income
        )
